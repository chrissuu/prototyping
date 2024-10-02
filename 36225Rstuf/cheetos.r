probability_list <- list()
trial_max = 10
for (k in 1:trial_max) {
prob <- 0
for (i in 1:k) {
prob <- prob + (0.6)**(i-1) * 0.4
}
probability_list <- append(probability_list, 1 - prob)
}
plot(1:trial_max, probability_list, main = "Probability of Catching 0 Cheetos in k Trials", xlab = "k", ylab = "Probability")
q()
