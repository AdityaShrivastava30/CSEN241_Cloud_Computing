import concurrent.futures
import requests
import time

# Endpoint for the bot's API
BOT_API_URL = "http://10.101.54.43:8080/function/chatbot-service"

def send_bot_query(payload):
    """Sends payload to the bot's API endpoint and returns the HTTP status code."""
    try:
        result = requests.post(BOT_API_URL, data=payload)
        return result.status_code
    except Exception as error:
        return str(error)

def execute_load_test(requests_per_second, test_duration_seconds=10):
    """Executes a load test by sending requests in parallel for a specified duration."""
    with concurrent.futures.ThreadPoolExecutor() as pool:
        tasks = []
        test_start = time.time()
        
        # Keep sending requests based on the specified rate and duration
        while time.time() - test_start < test_duration_seconds:
            for _ in range(requests_per_second):
                task = pool.submit(send_bot_query, "What's the weather like?")
                tasks.append(task)
            time.sleep(1)  # Delay to match the request rate per second

        outcomes = [task.result() for task in tasks]

    # Calculate and display the success metrics
    successes = [outcome for outcome in outcomes if outcome == 200]
    print(f"Total requests made: {len(outcomes)}")
    print(f"Successful requests: {len(successes)}")
    print(f"Success rate: {(len(successes) / len(outcomes)) * 100:.2f}%")

# Example usage
load_test_rate = 5  # This can be adjusted to simulate different scenarios
execute_load_test(load_test_rate)
