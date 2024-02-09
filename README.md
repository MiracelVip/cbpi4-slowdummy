# SlowDummy Sensor Plugin for CraftBeerPi

The `SlowDummy` sensor plugin for CraftBeerPi simulates sensor data by generating values that increase, decrease, or stabilize over time. It's designed to help test and demonstrate the functionality of the CraftBeerPi system without the need for actual sensor hardware. The value changes are randomized to mimic real-world sensor behavior in a predictable manner.

## Features

- **Simulated Sensor Data:** Generates sensor values that increase, decrease, or remain stable over randomized intervals.
- **Phase Cycling:** Simulates different phases of sensor readings (increasing, stable, decreasing) with random durations for each phase.

## Functionality

Upon activation, the `SlowDummy` sensor starts in an increasing phase, where its value gradually goes up. After reaching the end of a phase, characterized by a random number of cycles, it switches to the next phase. The cycle goes from increasing to stable (where the value does not change), to decreasing, and then back to increasing. Each phase lasts for a random number of cycles between 20 to 60 updates before transitioning.

## Configuration

There are no additional configurations required for this plugin beyond the standard setup within CraftBeerPi. The sensor's behavior is fully automated and managed internally by the plugin.

## Usage

To use the `SlowDummy` sensor in your CraftBeerPi setup:

1. Include the plugin in your CraftBeerPi installation.
2. No additional setup or configuration is required. The sensor will automatically start simulating data once CraftBeerPi is running.

## Conclusion

The `SlowDummy` sensor provides a useful tool for testing and demonstrating CraftBeerPi's sensor data handling capabilities without the need for physical hardware. Its simulated data output can help in developing and troubleshooting various components and plugins within the CraftBeerPi ecosystem.
