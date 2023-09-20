def run_timing():
    # This function takes no input and returns an average of 5km run times
    # It will continue to ask for input until the user enters an empty string
    # The function will return an average of the times and the number of times
    # entered

    # Initialize a variable to store the total time
    total_time = 0
    # Initialize a variable to store the number of runs
    runs_amount = 0
    # Initialize a list to store the times entered
    run_times = []

    # Continue to ask for input until the user enters an empty string
    while True:
        # Ask for input
        time = input('Enter 5km run time or press ENTER to finish: ')
        # Check if the input is empty
        if time == '':
            # Break out of the loop if the input is empty
            break
        # Add the time to the run_times list
        run_times.append(float(time))
        # Add the time to the total time
        total_time += float(time)
        # Increase the number of runs by 1
        runs_amount += 1
    # Calculate the average time
    average_time = total_time / runs_amount
    # Return the average time and the number of runs
    return average_time, runs_amount


# Call the run_timing function and store the returned values in average and number_of_runs
average, number_of_runs = run_timing()
# Print the results
print(f'Average of {average}, over {number_of_runs} runs.')
