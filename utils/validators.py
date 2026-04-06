def validate_telemetry(df):
    required = ["speed", "throttle", "brake"]

    for col in required:
        if col not in df.columns:
            return False, f"Missing column: {col}"

    return True, "OK"