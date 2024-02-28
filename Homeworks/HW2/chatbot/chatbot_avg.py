import requests
import time

# Endpoint URL for the chatbot service
BOT_SERVICE_URL = "http://10.101.54.43:8080/function/chatbot"

def calculate_avg_latency(payload, iterations=1):
    """Calculates the latency of a request or the average latency over several iterations."""
    cumulative_time = 0
    for _ in range(iterations):
        start = time.time()
        response = requests.post(BOT_SERVICE_URL, data=payload)
        finish = time.time()
        cumulative_time += (finish - start)
        if iterations == 1:  # Directly return the latency for a single iteration
            return finish - start
    return cumulative_time / iterations  # Return the average latency over multiple iterations

def main():
    # Evaluating response times under different conditions
    # a. Initial query without invoking figlet
    latency_without_figlet_initial = calculate_avg_latency("How are you?")
    print(f"a. Response time for the first request (no figlet): {latency_without_figlet_initial:.4f} seconds")

    # b. Follow-up query without invoking figlet
    latency_without_figlet_followup = calculate_avg_latency("How are you?")
    print(f"b. Response time for the second request (no figlet): {latency_without_figlet_followup:.4f} seconds")

    # c. Average latency over multiple queries not invoking figlet
    average_latency_without_figlet = calculate_avg_latency("How are you?", iterations=10)
    print(f"c. Average response time over 10 requests (no figlet): {average_latency_without_figlet:.4f} seconds")

    # d. Initial query invoking figlet
    latency_with_figlet_initial = calculate_avg_latency("Create a figlet for Hello")
    print(f"d. Response time for the first request (with figlet): {latency_with_figlet_initial:.4f} seconds")

    # e. Follow-up query invoking figlet
    latency_with_figlet_followup = calculate_avg_latency("Create a figlet for Hello")
    print(f"e. Response time for the second request (with figlet): {latency_with_figlet_followup:.4f} seconds")

    # f. Follow-up query invoking figlet after an initial query without it
    # Execute initial query without figlet
    calculate_avg_latency("How are you?")
    # Then measure latency for follow-up query with figlet
    latency_with_figlet_after_without = calculate_avg_latency("Create a figlet for Hello")
    print(f"f. Response time for the second request (with figlet, after no figlet): {latency_with_figlet_after_without:.4f} seconds")

    # g. Average latency for multiple queries invoking figlet
    average_latency_with_figlet = calculate_avg_latency("Create a figlet for Hello", iterations=10)
    print(f"g. Average response time over 10 requests (with figlet): {average_latency_with_figlet:.4f} seconds")

if __name__ == "__main__":
    main()
