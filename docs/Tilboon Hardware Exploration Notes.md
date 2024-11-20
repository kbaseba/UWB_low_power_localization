**Localization techniques Summary:**

| Technology | Accuracy | Range | Power Consumption | Cost | Use Cases |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **UWB** | \~10-30 cm | 10-100 meters | Moderate (High during Tx) | Higher | Precise localization, industrial automation |
| **BLE** | \~1-5 meters | 100-200 meters | Low | Low | Asset tracking, indoor navigation |
| **Wi-Fi** | \~5-15 meters | 100-300 meters | High | Moderate | Large-area tracking, location-based services |
| **Zigbee** | \~5-10 meters | 50-100 meters (mesh) | Low | Low | Mesh-based, low-power tracking |
| **RFID** | \~1 meter (passive) | 1-10 meters (active) | Very low (passive) | Very low | Inventory tracking, proximity-based detection |

Potentially \- backscatter (reflected/non-reflected signal)?

**Potential UWB Chip Study**

| UWB Module | Sleep Mode | Low-Power Listening | Active Mode (Tx/Rx) | Max Range | Accuracy | Pros | Cons |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Murata LBUA5QJ2AB-828** | \<1 µA | \~10-20 µA | 40-100 mA | \~100 meters | \~10-30 cm | \- Good accuracy.  \- Integrated solution for communication and localization. | \- High active power consumption. \- Relatively short range compared to others. |
| **Decawave DW1000** | \<1 µA | \~15 µA | 40-90 mA | \~300 meters | \~10 cm | \-Industry-standard with robust support. \- Long range. \- High accuracy. | \- Higher power consumption during low-power listening. \- Active mode power is higher compared to newer models. |
| **Decawave DW3220 (DW3000)** | \<1 µA | \~5 µA | 35-70 mA | \~200 meters | \~10 cm | \- Lower power consumption in both active and listening modes. \- High accuracy. \- Interoperable with newer UWB devices (e.g., Apple U1). | \- Slightly lower range than DW1000. \- More expensive due to newer technology. |
| **NXP SR040 / SR150** | \<1 µA | \~5 µA | 40-70 mA | \~200 meters | \~10-30 cm | \- Low power consumption in sleep and listening modes. \- Accurate positioning. | \- Ecosystem and development tools less mature than Decawave. \- Moderate range. |
| **Qorvo QM33100 / 130** | \<1 µA | \~10 µA | 35-60 mA | \~200 meters | \~10-20 cm | \- Lower power consumption compared to QM33120W. \- Designed for IoT and low-power applications. | \- Less widely adopted. \- Limited documentation and community support. |
| **Alteros ALPS UWB** | \<1 µA | \~7 µA | 30-50 mA | \~150 meters | \~10-30 cm | \- Very low power consumption during active and idle modes. \- Suitable for ultra-low-power applications. | \- Shorter range compared to other modules. \- Less community and support available. \- Niche product. |

**UWB Chip Current Profile (QM33120W)**

| Mode | Current Consumption |
| :---- | :---- |
| **Active (Transmission)** | 40-100 mA |
| **Active (Receiving)** | 40-70 mA |
| **Idle/Standby Mode** | 1-10 µA |
| **Sleep Mode** | \<1 µA |

