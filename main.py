import submer_collector
import examon_collector
import examon_publisher
import time

if __name__ == "__main__":
    while True:
        # Collect data from the submer API endpoints
        live_data = submer_collector.collect_live_measurements()
        average_data = submer_collector.collect_average_measurements()
        config_data = submer_collector.collect_configuration()

        print("Data collected from Submer API.")
        # print(live_data)
        # print(average_data)
        # print(config_data)
        examon_publisher.publish_to_examon(live_data)
        time.sleep(60)  # Sleep for 10 seconds before collecting data again