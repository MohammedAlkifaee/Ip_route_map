import webbrowser
import os
import requests
import subprocess
import platform
thislist = []
html_content2 = ""
i=1
ipss = []
ip_pairs_dict = {}
def get_router_ips(domain):
    command = ['tracert', domain]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        lines = result.stdout.splitlines()
        for line in lines:
            if "Tracing route to" in line:
                start_idx = line.index('[') + 1
                end_idx = line.index(']')
                first_destination_ip = line[start_idx:end_idx]
                break

        for line in lines:
            if any(char.isdigit() for char in line):
                parts = line.split()
                for part in parts:
                    if part.count('.') == 3:
                        ipss.append(part)
                        try:
                            response = requests.get(f"http://ip-api.com/json/{part}")
                            data = response.json()

                            if data["status"] == "success":
                                ip_pairs_dict[part] = {
                                    "lat": data["lat"],
                                    "lng": data["lon"]
                                }
                            else:
                                print("")
                        except Exception as e:
                            print("")
                            return None
    else:
        print("Error running the command:", result.stderr)


# Step 2: Write HTML to a file

lhost=""
ascii_art = """
****************************************************************************************************
*  _   _ _   _ _____     _______ ____  ____ ___ _______   __   ___  _____   _  ___   _ _____ _     *
* | | | | \ | |_ _\ \   / / ____|  _ \/ ___|_ _|_   _\ \ / /  / _ \|  ___| | |/ / | | |  ___/ \    *
* | | | |  \| || | \ \ / /|  _| | |_) \___ \| |  | |  \ V /  | | | | |_    | ' /| | | | |_ / _ \   *
* | |_| | |\  || |  \ V / | |___|  _ < ___) | |  | |   | |   | |_| |  _|   | . \| |_| |  _/ ___ \  *
*  \___/|_| \_|___|  \_/  |_____|_| \_\____/___| |_|   |_|    \___/|_|     |_|\_\\___/|_|/_/   \_\ *
****************************************************************************************************
                         by Dr.Fahad galib  & Mohammad Abbas Shareef
"""
print(ascii_art)
while True:
    print("\nPlease choose an option:")
    print("1. Set your Destenation website or Host")
    print("2. Get Ip Route with Glocation")
    print("3. Generate the route on Map")
    print("4. Exit")
    choice = input("\nEnter your choice: ")

    if choice == '1':

        lhost = input("Enter your Destenation website ")
        domain = lhost
        router_ips = get_router_ips(domain)
        print("Secssesfully")

    elif choice == '2':
        print("IP_Router     lat         lng")
        items = list(ip_pairs_dict.items())
        if items:
            first_item = items[0]
            first_ip = first_item[0]
            for ip, data in items[1:]:
                a = data["lat"]
                b = data["lng"]
                print(ip, "      ", a, "      ", b)
            a = first_item[1]["lat"]
            b = first_item[1]["lng"]
            print(first_ip, "      ", a, "      ", b)
        else:
            print("No records found in ip_pairs_dict.")



    elif choice == '3':
        html_content1 = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>World Map with Line and Bigger Points</title>
            <style>
                #map {
                    height: 100%;
                    width: 100%;
                }
                html, body {
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }
            </style>
        </head>
        <body>
            <h1><center>Buld by Dr.Fahad galib  & Mohammad Abbas Shareef</center></h1>
            <div id="map"></div>

            <script>
                function initMap() {
                    // Create the map centered at the middle of the world
                    var worldCenter = {lat: 20, lng: 0}; // World center coordinates
                    var map = new google.maps.Map(document.getElementById('map'), {
                        zoom: 2,  // World view zoom level
                        center: worldCenter
                    });

                    // Define the points (with their latitude and longitude)
                    var points = [
        """
        items = list(ip_pairs_dict.items())
        first_item = items[0]
        for ip, data in items:
            a = data["lat"]
            b = data["lng"]
            html_content2 += f"{{lat: {a}, lng: {b}}},\n"

        html_content3 = """
                    ];

                    // Loop to add larger markers for each point
                    for (let i = 0; i < points.length; i++) {
                        new google.maps.Marker({
                            position: points[i],
                            map: map,
                            icon: {
                                url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",  // Custom icon (blue marker)
                                scaledSize: new google.maps.Size(50, 50)  // Make the marker larger (50x50 px)
                            }
                        });
                    }

                    // Loop to draw lines (polylines) between consecutive points
                    for (let i = 0; i < points.length - 1; i++) {
                        var line = new google.maps.Polyline({
                            path: [points[i], points[i + 1]],  // Draw line between current and next point
                            geodesic: true,  // To draw a curved line on the earth's surface
                            strokeColor: '#FF0000',  // Line color (red)
                            strokeOpacity: 1.0,
                            strokeWeight: 2 // Line thickness
                        });
                        // Add the line to the map
                        line.setMap(map);
                    }
                }
            </script>

            <script async defer
                src="https://maps.googleapis.com/maps/api/js?key=YOURAPIKEY&callback=initMap">
            </script>
        </body>
        </html>
        """
        file_path = "sample_page.html"
        with open(file_path, "w") as file:
            file.write(html_content1 + html_content2 + html_content3)
        full_path = os.path.abspath(file_path)
        webbrowser.open(f"file://{full_path}")
    elif choice == '4':
        print("Good bye")
        break
    else:
        print("please choise correct one")
