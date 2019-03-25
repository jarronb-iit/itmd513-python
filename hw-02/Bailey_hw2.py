"""
Name: Jarron Bailey
Assignment: Homework 2
Date: 02/04/2019
Description: Designed a program that follows the procedures for troubleshooting diesel engines 
"""

# Check engine light color


def troubleshoot_diesel_engine():
    engine_status_light_color = input(
        "What color is the check engine status light?: ")
    engine_status_light_color = engine_status_light_color.lower()

    # Send color to the engine color checker function
    engine_status_light_switch(engine_status_light_color)

    # Program is finished
    return print("\n ... Program finished")


def engine_status_light_switch(engine_status_light_color):
    if engine_status_light_color == "green":
        return print("\nPlease do a restart procedure.")
    elif engine_status_light_color == "amber":
        return print("\nPlease perform the check fuel line service routine.")
    elif engine_status_light_color == "red":
      # if red start the red light troubleshooting procedure
        return red_status_procedure()


def red_status_procedure():
    print("Please shut off all input lines and check meter #3.")
    meter_reading = input("Enter meter reading: ")
    meter_reading = int(meter_reading)
    if meter_reading < 50:
        return check_main_line()
    elif meter_reading >= 50:
        measure_flow_velocity()

# Check main line if meter reading is < 50


def check_main_line():
    print("Please check main line and test pressure.")
    pressure = input("Enter pressure(normal, high, low): ")
    pressure = pressure.lower()
    if pressure == "normal":
        return print("\nPlease refer to the motor service manual.")
    elif pressure == "high" or "low":
        return print("\nPlease refer to the main line service manual.")

# measure velocity if meter reading is >= 50


def measure_flow_velocity():
    print("\nPlease measure the flow velocity")
    velocity = input("Enter velocity(normal, high, or low): ")
    velocity = velocity.lower()
    if velocity == "normal":
        return print("\nPlease refer to the inlet service manual.")
    elif velocity == "high" or "low":
        return print("\nPlease refer unit for factory service.")


# Run troubleshooting function
troubleshoot_diesel_engine()
