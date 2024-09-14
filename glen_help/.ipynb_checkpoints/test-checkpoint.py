def param_shift_estimator_gradient(circuit: QuantumCircuit,
                                   input_params: np.ndarray,
                                   weight_params: np.ndarray,
                                   estimator: BaseEstimatorV2,
                                   observables: BaseOperator
) -> np.ndarray:
    """
    Compute the gradients of the expectation values using the parameter shift rule for multiple observables.

    Args:
        circuit: Circuit consisting of data loader gates and the neural network ansatz.
        input_params: Data encoding parameters.
        weight_params: Neural network ansatz parameters.
        estimator: EstimatorV2 primitive.
        observables: List of observables to compute the expectation values over.

    Returns:
        weight_gradients: Array of shape (num_samples, num_weight_params, num_observables) containing the gradients.
    """
    num_samples = input_params.shape[0]
    num_weight_params = len(weight_params)
    num_observables = len(observables)
    shift = np.pi / 2  # parameter shift value

    weights = np.broadcast_to(weight_params, (num_samples * num_weight_params, num_weight_params))
    inputs  = np.tile(input_params, (num_weight_params, 1))

    weights_plus = weights.copy()
    weights_minus = weights.copy()
    for j in range(num_weight_params):
        for i in range(num_samples):
            weights_plus[j * num_samples + i][j] = weight_params[j] + shift
            weights_minus[j * num_samples + i][j] = weight_params[j] - shift

    params_plus = np.concatenate((inputs, weights_plus), axis=1)
    params_minus = np.concatenate((inputs, weights_minus), axis=1)

    # Create a list of (circuit, observable, params) tuples for the estimator
    # If observables is a single observable, make it a list for consistency
    if isinstance(observables, BaseOperator):
        observables = [observables]

    if len(observables) == 1:
        pub_plus = (circuit, observables, params_plus)
        pub_minus = (circuit, observables, params_minus)
        # Run the estimator and get the results
        job = estimator.run([pub_plus, pub_minus])
    else:  
        pub_plus = [(circuit, observables, p) for p in params_plus]
        pub_minus = [(circuit, observables, p) for p in params_minus]
        job = estimator.run(pub_plus + pub_minus)

    results = job.result()
    num_pub_plus = len(pub_plus)
    result_plus = results[:num_pub_plus]
    result_minus = results[num_pub_plus:]
   
    # Extract expectation values from results
    if len(observables) == 1:
        expectation_values_plus = results[0].data.evs
        expectation_values_minus = results[1].data.evs
    else:
        expectation_values_plus = np.array([res.data.evs for res in result_plus])
        expectation_values_minus = np.array([res.data.evs for res in result_minus])

    weight_gradients = np.zeros((num_samples, num_weight_params, num_observables))

    weight_gradients = (expectation_values_plus - expectation_values_minus) / (2)
    if len(observables) == 1:
        weight_gradients = np.array(weight_gradients).reshape((num_weight_params, num_samples)).T
    else:
        weight_gradients = np.array(weight_gradients).reshape((num_weight_params, num_samples, num_observables)).T
   
    return weight_gradients


------


def cost_and_grad_function_estimator(weight_params):
    """
    Cost and the gradient function for the optimizer to update the ansatz parameters.

    Args:
        weight_params: ansatz parameters to be updated by the optimizer.

    Output:
        cost: MSE loss.
        gradients: gradient of the MSE loss with respect to weight parameters.
    """
    predictions = forwardEstimator(circuit=circuit,
                          input_params=input_params,
                          weight_params=weight_params,
                          estimator=estimator,
                          observables=observables)
   
    cost = mse_loss(predict=predictions, target=target)
    objective_func_vals.append(cost)

    gradients = param_shift_estimator_gradient(circuit=circuit,
                                               input_params=input_params,
                                               weight_params=weight_params,
                                               estimator=estimator,
                                               observables=observables)

    # Check if gradients need to be transposed or reshaped
    if gradients.shape[0] != gradients.shape[1]:  # Check if it's a square matrix
        gradients = gradients.T  # Ensure shape is (n_classes, n_parameters)
       
    print("Shape of prediction:", predictions.shape)
    print("Shape of target:", target.shape)
    # Gradients of the MSE loss
    diff = predictions - target # Shape (n_samples, n_classes)

    # Average over the first dimension
    gradient_avg = np.mean(gradients, axis=1)  # Shape (n_parameters, n_classes)
    gradient_vector = (diff @ gradient_avg.T) * 2
 
    print("Shape of diff:", diff.shape)  # Should be (batch_size, n_classes)
    print("Shape of gradients:", gradients.shape)  # Should be (batch_size, n_parameters, n_classes)
    print("Shape of gradient_avg:", gradient_avg.T.shape)  # Should be (n_classes, n_parameters)
    print("Shape of gradient_vector:", gradient_vector.shape)  # Should be (n_parameters,)

    # Aggregating Gradients
    # For Consistency: The mean is generally preferred because it normalizes the gradient across samples, ensuring that the gradient update is consistent regardless of the batch size.
    # For Batch Processing: If you’re using mini-batches, averaging gradients from each mini-batch is standard practice. This helps in making the gradient updates stable and representative of the entire dataset.
    gradient_vector = np.mean(gradient_vector, axis=0)  # Should be (n_parameters,)

    # Sum of Gradients:
    # What It Is: Instead of averaging, you sum the gradients over all samples or batches.
    # Why Use It: Summing can be used if you want to accumulate the gradients before applying them, which might be useful in some batch processing scenarios.
    # When to Use: This approach is less common but can be appropriate if you are accumulating gradients over several batches before applying updates.
    #gradient_vector = np.sum(gradient_vector, axis=0)  # Should be (n_parameters,)
    print("Shape of gradient_vector:", gradient_vector.shape)  # Should be (n_parameters,)

    global iter
    print(f"Iter: {iter}, loss: {cost}")
    iter += 1

    return cost, gradient_vector