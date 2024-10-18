def validaEventSchema(jsonData2Validate):
    print(dict(jsonData2Validate))
    # Required structure for Event Schema
    required_structure = {
        "Person": {"Name": "", "Occupation": ""},
        "Location": {"City": ""},
        "Event": {"Date": ""}
    }
    
    # Helper function to check required structure recursively
    def check_required_fields(data, required):
        # Ensure the data is a dictionary
        if not isinstance(data, dict):
            return False, "Data should be a dictionary"

        for key, value in required.items():
            if key not in data:
                return False, f"Missing key: {key}"

            # If the value is a dictionary, recurse into it
            if isinstance(value, dict):
                valid, msg = check_required_fields(data[key], value)
                if not valid:
                    return False, msg
            else:
                # Ensure that the key's value is not empty or null
                if not data[key]:
                    return False, f"Key '{key}' is missing a value"

        return True, "Valid"

    # Validate the structure
    is_valid, message = check_required_fields(jsonData2Validate, required_structure)
    return is_valid, message


def validateJobSchema(jsonData2Validate):
    # Required structure for Job Schema
    required_structure = {
        "Person": {"Name": ""},
        "Task": {"Duration": "", "Client": "", "Date": ""}
    }
    
    # Helper function to check required structure recursively
    def check_required_fields(data, required):
        # Ensure the data is a dictionary
        if not isinstance(data, dict):
            return False, "Data should be a dictionary"

        for key, value in required.items():
            if key not in data:
                return False, f"Missing key: {key}"

            # If the value is a dictionary, recurse into it
            if isinstance(value, dict):
                valid, msg = check_required_fields(data[key], value)
                if not valid:
                    return False, msg
            else:
                # Ensure that the key's value is not empty or null
                if not data[key]:
                    return False, f"Key '{key}' is missing a value"

        return True, "Valid"

    # Validate the structure
    is_valid, message = check_required_fields(jsonData2Validate, required_structure)
    return is_valid, message


# Valid Event data
event_data = {
    "Person": {"Name": "John", "Occupation": "Engineer"},
    "Location": {"City": "New York"},
    "Event": {"Date": "2024-01-01"}
}

# Validate Event Schema
is_valid, message = validaEventSchema(event_data)
print(is_valid, message)  # Output: True, "Valid"

# Invalid Event data (missing keys)
invalid_event_data = {
    "Person": {"Name": "John"},
    "Location": {"City": "New York"}
    # Missing 'Event' key and 'Occupation'
}

is_valid, message = validaEventSchema(invalid_event_data)
print(is_valid, message)  # Output: False, "Missing key: Event"

# Valid Job data
job_data = {
    "Person": {"Name": "Alice"},
    "Task": {"Duration": "5 hours", "Client": "ABC Corp", "Date": "2024-10-17"}
}

# Validate Job Schema
is_valid, message = validateJobSchema(job_data)
print(is_valid, message)  # Output: True, "Valid"





