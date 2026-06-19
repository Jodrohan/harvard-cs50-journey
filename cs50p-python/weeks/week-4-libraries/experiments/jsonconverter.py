'''
Log-to-JSON Parser
1. You have a raw string containing multiple logs: 
   "user:rohan,action:login,status:success;user:sita,action:delete,status:fail"
2. Your goal: Parse this string into a list of dictionaries.
3. Final Structure: 
   [
     {"user": "rohan", "action": "login", "status": "success"},
     {"user": "sita", "action": "delete", "status": "fail"}
   ]

Pseudo-code:
    - INITIALIZE empty_list
    - SPLIT the raw_string by ';' to get individual log entries
    - FOR each entry IN entries:
        - INITIALIZE empty_dict
        - SPLIT entry by ',' to get key:value pairs
        - FOR each pair IN pairs:
            - SPLIT pair by ':' to get key and value
            - ASSIGN value TO dict[key]
        - APPEND dict TO empty_list
    - PRINT empty_list
'''
def main():
    raw_log_data = "user:rohan,action:login,status:success;user:sita,action:delete,status:fail;user:admin,action:upload,status:success;user:guest,action:login,status:fail"
    log_list = []
    entries = raw_log_data.split(";")
    for entry in entries:
        empty_dict = {}
        key_value = entry.split(",")
        
        for pair in key_value:
           
            key, value = pair.split(":")
            empty_dict[key] = value
        log_list.append(empty_dict)
    print(log_list)
if __name__ == "__main__":
    main()