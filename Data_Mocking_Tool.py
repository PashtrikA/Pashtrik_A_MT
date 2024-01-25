import requests
import json
import time
import random
import datetime
import threading


def update_submodel_element(port, submodelID, idShortPath, updatedValue):
    url = f"http://localhost:{port}/submodels/{submodelID}/submodel-elements/{idShortPath}/$value?level=core"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = f'"{updatedValue}"'

    try:
        response = requests.patch(url, headers=headers, data=data)

        if response.status_code == 204:
            print(f"Update successful for {idShortPath} with value {updatedValue}")
        else:
            print(f"Failed to update {idShortPath} with value {updatedValue}. Status code: {response.status_code}\nResponse: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request exception for {idShortPath} with value {updatedValue}: {e}")

def generate_fault_code_readings(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        fault_code = f"{random.randint(1, 4):03d}"
        update_submodel_element(port, submodelID, "FaultCodeReadings.Code", fault_code)

        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "FaultCodeReadings.Timestamp", timestamp)

        update_submodel_element(port, submodelID, "FaultCodeReadings.Status", "Active")

        time.sleep(10)

        update_submodel_element(port, submodelID, "FaultCodeReadings.Status", "Not Active")

        time.sleep(random.randint(5, 15))

def generate_vehicle_health_monitoring(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        parameters = {
            "Engine Temperature": {"range": (90, 100), "unit": "degC"},
            "Oil Pressure": {"range": (30, 60), "unit": "psi"},
            "Battery Voltage": {"range": (13, 14), "unit": "V"},
            "Tire Pressure": {"range": (30, 35), "unit": "psi"}
        }
        timestamp = datetime.datetime.now().isoformat()

        for index, (param_name, param_details) in enumerate(parameters.items()):
            min_val, max_val = param_details["range"]
            unit = param_details["unit"]
            value = f"{random.randint(min_val, max_val)} {unit}"
            update_submodel_element(port, submodelID, f"VehicleHealthMonitoring.Parameters[{index}].Parameter", param_name)
            update_submodel_element(port, submodelID, f"VehicleHealthMonitoring.Parameters[{index}].Value", value)
            update_submodel_element(port, submodelID, f"VehicleHealthMonitoring.Parameters[{index}].TimeStamp", timestamp)

        time.sleep(random.randint(5, 15))

def generate_data_transmission_logs(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        data_size = f"{random.randint(100, 1000)}KB"
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "DataTransmissionLogs.Activity", "Data Sent to Cloud")
        update_submodel_element(port, submodelID, "DataTransmissionLogs.DataSize", data_size)
        update_submodel_element(port, submodelID, "DataTransmissionLogs.TimeStamp", timestamp)
        time.sleep(random.randint(5, 15))


def generate_remote_operation_logs(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        operation = random.choice(["Vehicle Locked", "Vehicle Unlocked"])
        status = random.choice(["Success", "Failure"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "RemoteOperationLogs.Operation", operation)
        update_submodel_element(port, submodelID, "RemoteOperationLogs.Status", status)
        update_submodel_element(port, submodelID, "RemoteOperationLogs.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))


def generate_braking_event_records(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        context = random.choice(["Emergency Stop", "Regular Stop", "Sudden Stop"])
        severity = random.choice(["High", "Medium", "Low"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "BrakingEventRecords.Context", context)
        update_submodel_element(port, submodelID, "BrakingEventRecords.Severity", severity)
        update_submodel_element(port, submodelID, "BrakingEventRecords.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_usage_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        activity = random.choice(["Navigation to Destination", "Music Playback", "Voice Command"])
        duration = f"{random.randint(5, 120)} minutes"
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "UsageData.Activity", activity)
        update_submodel_element(port, submodelID, "UsageData.Duration", duration)
        update_submodel_element(port, submodelID, "UsageData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_voice_interaction_logs(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        command = random.choice(["Navigate to Home", "Play Music", "Set Climate to 21 degC"])
        response = f"Setting {command.lower()}"
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "VoiceInteractionLogs.Command", command)
        update_submodel_element(port, submodelID, "VoiceInteractionLogs.Response", response)
        update_submodel_element(port, submodelID, "VoiceInteractionLogs.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_real_time_communication_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        data_rate = f"{random.choice([100, 150, 200])} Mbps"
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "RealTimeCommunicationData.DataRate", data_rate)
        update_submodel_element(port, submodelID, "RealTimeCommunicationData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_energy_usage_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        energy_consumed = f"{random.randint(5, 20)} kWh"
        driving_mode = random.choice(["Eco", "Sport", "Normal"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "EnergyUsageData.EnergyConsumed", energy_consumed)
        update_submodel_element(port, submodelID, "EnergyUsageData.DrivingMode", driving_mode)
        update_submodel_element(port, submodelID, "EnergyUsageData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_energy_recovery_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        braking_event = random.choice(["Moderate Stop", "Emergency Stop", "Gentle Stop"])
        energy_recovered = f"{random.uniform(0.5, 2.0):.1f} kWh"
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "EnergyRecoveryData.BrakingEvent", braking_event)
        update_submodel_element(port, submodelID, "EnergyRecoveryData.EnergyRecovered", energy_recovered)
        update_submodel_element(port, submodelID, "EnergyRecoveryData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_mode_selection_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        current_drive_mode = random.choice(["Eco", "Sport", "Comfort"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "ModeSelectionData.CurrentDriveMode", current_drive_mode)
        update_submodel_element(port, submodelID, "ModeSelectionData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_maintenance_alerts(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        next_maintenance_date = (datetime.datetime.now() + datetime.timedelta(days=random.randint(30, 180))).date().isoformat()
        last_maintenance_date = (datetime.datetime.now() - datetime.timedelta(days=random.randint(30, 180))).date().isoformat()
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "MaintenanceAlerts.NextScheduledMaintenance", next_maintenance_date)
        update_submodel_element(port, submodelID, "MaintenanceAlerts.LastMaintenance", last_maintenance_date)
        update_submodel_element(port, submodelID, "MaintenanceAlerts.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_wear_and_tear_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        components = ["Brake Pads", "Tires", "Engine Oil"]
        timestamp = datetime.datetime.now().isoformat()
        for index, component in enumerate(components):
            replacement_interval = f"{random.randint(50, 100)}%"
            update_submodel_element(port, submodelID, f"WearAndTearData.WearAndTearDataList[{index}].Component", component)
            update_submodel_element(port, submodelID, f"WearAndTearData.WearAndTearDataList[{index}].ReplacementInterval", replacement_interval)
            update_submodel_element(port, submodelID, f"WearAndTearData.WearAndTearDataList[{index}].LastChecked", timestamp)
        time.sleep(1)

def generate_climate_and_comfort_adjustment_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        temperature_setting = f"{random.randint(16, 28)}degC"
        seat_heating = random.choice(["1", "2", "3"])
        air_flow_speed = random.choice(["1", "2", "3"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "ClimateAndComfortAdjustmentData.TemperatureSetting", temperature_setting)
        update_submodel_element(port, submodelID, "ClimateAndComfortAdjustmentData.SeatHeating", seat_heating)
        update_submodel_element(port, submodelID, "ClimateAndComfortAdjustmentData.AirFlowSpeed", air_flow_speed)
        update_submodel_element(port, submodelID, "ClimateAndComfortAdjustmentData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_lighting_adjustment_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        color = random.choice(["Blue", "Green", "Purple", "Red"])
        intensity = random.choice(["Low", "Medium", "High"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "LightingAdjustmentData.Color", color)
        update_submodel_element(port, submodelID, "LightingAdjustmentData.Intensity", intensity)
        update_submodel_element(port, submodelID, "LightingAdjustmentData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_access_logs(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        method = random.choice(["Biometric Authentication", "Keyless Entry", "Remote Access"])
        user_id = f"User{random.randint(100, 999)}"
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "AccessLogs.Method", method)
        update_submodel_element(port, submodelID, "AccessLogs.UserID", user_id)
        update_submodel_element(port, submodelID, "AccessLogs.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))


def generate_authentication_logs(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        authentication_method = random.choice(["RFID", "Biometric", "PIN Code"])
        outcome = random.choice(["Successful", "Failed"])
        attempt_timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "AuthenticationLogs.AuthenticationMethod", authentication_method)
        update_submodel_element(port, submodelID, "AuthenticationLogs.Outcome", outcome)
        update_submodel_element(port, submodelID, "AuthenticationLogs.AttemptTimestamp", attempt_timestamp)
        time.sleep(random.randint(5, 15))

def generate_parking_event_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        location = f"ExampleLocation{random.randint(1, 20)}"
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "ParkingEventData.Location", location)
        update_submodel_element(port, submodelID, "ParkingEventData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_camera_feed_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        camera_location = random.choice(["Front", "Rear", "Left Side", "Right Side"])
        status = random.choice(["Active", "Inactive"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "CameraFeedData.CameraLocation", camera_location)
        update_submodel_element(port, submodelID, "CameraFeedData.Status", status)
        update_submodel_element(port, submodelID, "CameraFeedData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))

def generate_current_user_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        user = random.choice(["Driver 1", "Driver 2", "Passenger"])
        seat_position = random.choice(["Position 1", "Position 2", "Position 3"])
        climate_control = f"{random.randint(18, 26)}degC"
        update_submodel_element(port, submodelID, "CurrentUser.User", user)
        update_submodel_element(port, submodelID, "CurrentUser.SeatPosition", seat_position)
        update_submodel_element(port, submodelID, "CurrentUser.ClimateControl", climate_control)
        time.sleep(random.randint(5, 15))

def generate_assistance_utilization_data(port, submodelID):
    time.sleep(random.uniform(0, 10))
    while True:
        feature = random.choice(["Adaptive Cruise Control", "Lane Keeping Assist", "Automatic Parking"])
        status = random.choice(["Engaged", "Disengaged"])
        timestamp = datetime.datetime.now().isoformat()
        update_submodel_element(port, submodelID, "AssistanceUtilizationData.Feature", feature)
        update_submodel_element(port, submodelID, "AssistanceUtilizationData.Status", status)
        update_submodel_element(port, submodelID, "AssistanceUtilizationData.Timestamp", timestamp)
        time.sleep(random.randint(5, 15))



if __name__ == "__main__":
    port = "8081"
    submodelID = "your_submodelID"

    # Creating threads for each function
    threads = [
        threading.Thread(target=generate_fault_code_readings, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMjA5Ml8wMTAxXzEwNDJfMTk2OQ==")),
        threading.Thread(target=generate_vehicle_health_monitoring, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMDM5Ml8wMTAxXzEwNDJfNjUyMw")),
        threading.Thread(target=generate_data_transmission_logs, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMzQ5Ml8wMTAxXzEwNDJfMTY0Ng")),
        threading.Thread(target=generate_remote_operation_logs, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMTAwM18wMTAxXzEwNDJfNzc4MA")),
        threading.Thread(target=generate_braking_event_records, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vNTM4Ml8wMjkwXzEwNDJfOTg2NA")),
        threading.Thread(target=generate_usage_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vNzM4Ml8wMjkwXzEwNDJfNTQ3Nw")),
        threading.Thread(target=generate_voice_interaction_logs, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMjAwM18wMjkwXzEwNDJfNDgzOQ")),
        threading.Thread(target=generate_real_time_communication_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMzM0M18wMTAxXzEwNDJfMzg0MQ")),
        threading.Thread(target=generate_energy_usage_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMDA1M18wMTAxXzEwNDJfNzgzNg")),
        threading.Thread(target=generate_energy_recovery_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vNzA1M18wMTAxXzEwNDJfMTk3Ng")),
        threading.Thread(target=generate_mode_selection_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vNTE1M18wMTAxXzEwNDJfOTUyNg")),
        threading.Thread(target=generate_maintenance_alerts, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMjI1M18wMTAxXzEwNDJfNTkxNA")),
        threading.Thread(target=generate_wear_and_tear_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vOTA2M18wMTAxXzEwNDJfNjczNg")),
        threading.Thread(target=generate_climate_and_comfort_adjustment_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vNzI1M18wMTAxXzEwNDJfOTYwOQ")),
        threading.Thread(target=generate_lighting_adjustment_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMzM1M18wMTAxXzEwNDJfMTIwNg")),
        threading.Thread(target=generate_access_logs, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMTQ1M18wMTAxXzEwNDJfNzkxMQ==")),
        threading.Thread(target=generate_authentication_logs, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vNzQ1M18wMTAxXzEwNDJfMzk0MA==")),
        threading.Thread(target=generate_parking_event_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMzU1M18wMTAxXzEwNDJfOTc5OA")),
        threading.Thread(target=generate_camera_feed_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vOTU1M18wMTAxXzEwNDJfNTg0NA")),
        threading.Thread(target=generate_current_user_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vNDA2M18wMTAxXzEwNDJfMzkyNw")),
        threading.Thread(target=generate_assistance_utilization_data, args=(port, "aHR0cHM6Ly91bmktc3R1dHRnYXJ0LmNvbS9pZHMvc20vMjM4Ml8wMjkwXzEwNDJfMTcyNw")),
    ]


    for thread in threads:
        thread.start()

