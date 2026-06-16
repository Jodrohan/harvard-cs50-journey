"""
MISSION: THE API BOUNTY HUNTER
-------------------------------------------------------------------------------
Scenario:
You are a bounty hunter tracking a digital fugitive hiding in a global server 
network. Write a script that takes the fugitive's name from the command line, 
"downloads" the global server directory via an API, and searches through the 
regions, data centers, and users to find them.

Specifications:
1. System Operations (sys):
   - The script must accept exactly ONE command-line argument: the target's 
     username (e.g., `python bounty.py neo`).
   - If the user forgets the name, or provides too many arguments, print a 
     strict usage error and gracefully exit using `sys.exit()`.

2. External Data (Mocking 'requests' & JSON):
   - Use the nested dictionary below to simulate the JSON payload you would 
     normally receive from `requests.get(url).json()`.

3. The Loop Labyrinth (Nested Loops & break):
   - Dig through the `regions`, then the `data_centers`, and finally the `users`.
   - As soon as the target username is found, print their exact location:
     "Target found in [Region Name], Center [Data Center Name]!"
   - Once found, cleanly `break` out of the search. Do not waste CPU cycles 
     searching the rest of the globe.

4. The Ultimate Fail-Safe (for...else):
   - If the script searches every single user across the entire network and 
     never finds the target, use the `for...else` construct on the outermost 
     loop to print: "Target not found in any region."
   - Terminate the script using `sys.exit()`.

Mock Data Payload:
-------------------------------------------------------------------------------
network_data = {
    "regions": [
        {
            "region_name": "US-East",
            "data_centers": [
                {"name": "Alpha", "users": ["alice", "bob", "charlie"]},
                {"name": "Beta",  "users": ["david", "eve", "frank"]}
            ]
        },
        {
            "region_name": "EU-West",
            "data_centers": [
                {"name": "Gamma", "users": ["grace", "heidi", "ivan"]},
                {"name": "Delta", "users": ["judy", "neo", "mallory"]}
            ]
        }
    ]
}
"""
import sys
def main():
    try:
        print("Enter target name: ", sys.argv[1])
    except IndexError:
        sys.exit()
    else:
        target = sys.argv[1]
    network_data = {
    "regions": [
        {
            "region_name": "US-East",
            "data_centers": [
                {"name": "Alpha", "users": ["alice", "bob", "charlie"]},
                {"name": "Beta",  "users": ["david", "eve", "frank"]}
            ]
        },
        {
            "region_name": "EU-West",
            "data_centers": [
                {"name": "Gamma", "users": ["grace", "heidi", "ivan"]},
                {"name": "Delta", "users": ["judy", "neo", "mallory"]}
            ]
        }
    ]
}
    target_found = False
    for region in network_data["regions"]:

        for center in region["data_centers"]:

            for user in center["users"]:
                if user == target:
                    print(f"Target found in {region["region_name"]}, center {center["name"]}")
                    target_found = True
                    break
            if target_found:
                break
        if target_found:
            break       
    else:
        print("Target not found: ")
        sys.exit()

if __name__ == "__main__":
    main()


