def analyze_logs(logs: list[str]) -> dict:
    stats = {"total": len(logs), "error": 0, "warning": 0}
    
    for line in logs:
        line_upper = line.upper()
        if "ERROR" in line_upper:
            stats["error"] += 1
        elif "WARNING" in line_upper:
            stats["warning"] += 1
            
    return stats