![image](https://github.com/user-attachments/assets/d8767441-7fdc-47bf-8571-e16888baa485)


# Router IP Geolocation Tool

## Description

The **Router IP Geolocation Tool** is a Python application that utilizes the `tracert` command to trace the route to a specified destination website or host. This tool extracts the IP addresses of the routers along the route and provides geolocation information for each public IP address. The geolocation data includes latitude and longitude, which can be visualized on a map generated using Google Maps.

### Features

1. **Set Destination**: Users can input a destination website or host to trace the route.
2. **Get IP Route with Geolocation**: The application retrieves the IP addresses of the routers along the route to the destination and fetches their geolocation data.
3. **Visualize Route on Map**: The tool generates an HTML file that displays a map with markers representing the IP addresses, along with lines connecting consecutive points.
4. **User-Friendly Interface**: The command-line interface prompts users to choose actions easily.

### Technologies Used

- **Python**: The programming language used to implement the application.
- **Subprocess**: Utilized to execute the `tracert` command.
- **Requests**: Used to make HTTP requests to fetch geolocation data from the `ip-api.com` API.
- **Google Maps API**: For visualizing the IP locations on a map.
- **HTML/CSS/JavaScript**: For generating the interactive map display.

### Usage

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/MohammadAlkifaee/Ip_route_map.git]
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd repository-name
   ```
3. **Install Required Libraries**:
   Ensure you have the `requests` library installed. You can install it using pip:
   ```bash
   pip install requests
   ```
4. **Run the Application**:
   Execute the script:
   ```bash
   python script_name.py
   ```

5. **Follow the prompts in the command line interface to set a destination, view IPs and geolocation, and generate the map**.

### Important Notes

- Ensure you have an active internet connection for the application to fetch geolocation data.
- Replace the Google Maps API key in the HTML generation section of the code with your own API key for the map to display correctly.
- The `tracert` command is specific to Windows; ensure the script is run on a Windows environment.

![image](https://github.com/user-attachments/assets/c60da55b-519e-4046-af87-3c8044a40864)


## Acknowledgments

- Inspired by Dr. Fahad Galib & Mohammad Abbas Shareef.



