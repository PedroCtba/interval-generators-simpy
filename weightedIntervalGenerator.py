# Make a weigted interval generator
class weightedIntervalGenerator:
    # Make the initial atributes and run initial methods
    def __init__(self, total_time, total_objects, window_size):
        # Store the total time | total of objects | window_size
        self.total_time = total_time
        self.total_objects = total_objects
        self.window_size = window_size

        # Make the normalized windows
        self.make_normalized_windows()

        # Define the timestamp and intial window as 0
        self.timestamp_counter = 0
        self.actual_window = 0

    # Define a method that makes a normalized window
    def make_normalized_windows(self):
        # Discover the number of windows
        _num_of_windows = self.total_time / self.window_size

        # Raise error in case of non integer
        if _num_of_windows % 1 > 0:
            raise ValueError("The division betwen total_time and window_size must return an integer")
        
        # Else, make the window list
        else:
            # Convert n of windows to integer
            _num_of_windows = int(_num_of_windows)

            # Discover the total of objects per window
            _total_objects_per_window = self.total_objects / _num_of_windows

            # Define the normalized windows as an atribute
            self.normalized_windows = [(int(_total_objects_per_window), window) for window in range(_num_of_windows)]

        return None

    # Define a method to set the weighted window edges as an atribute
    def return_all_weighted_windows_edges(self):
        self.weighted_edges = [edge[0] for edge in self.weighted_windows]

        return None

    # Define a method to set the weighted windows list as an attribute
    def make_weighted_windows(self, weights):
        # Verify if the sum of weights is equal to 1:
        if sum(weights) != 1:
            raise ValueError("The sum of the weights must be equal to 1")

        # Discover the normal windows individual weight and size
        n_weight = 1 / len(self.normalized_windows)
        n_window = self.normalized_windows[0][0]

        # Define the new window with its weights
        self.weighted_windows = [(((new_w*n_window)/n_weight), new_w) for new_w in weights]

        # Run the weighted edges method
        self.return_all_weighted_windows_edges()

        return None

    # Generate timestamp considering the window moment
    def generate_timestamp(self):
        # If the timestamp counter is very close to the current window size
        if (self.weighted_windows[self.actual_window][0] - self.timestamp_counter) < 1:

            # go to next window
            self.actual_window += 1

            # Set timestamp counter as 0
            self.timestamp_counter = 0

        # Increment this evertime this method is being used
        self.timestamp_counter += 1

        # Try to return the time with the actual window, prepare except to out of lenght list
        try:
            
            return (self.window_size * 60 / self.weighted_windows[self.actual_window][0])

        # If you got an IndexError, reset actual window to 0
        except IndexError:
            self.actual_window = 0
            return (self.window_size * 60 / self.weighted_windows[self.actual_window][0])