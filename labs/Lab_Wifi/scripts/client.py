import subprocess, re, statistics, time, sys 

def main(): 
    print("=== iperf Client Mode ===") 
    ip = input("Server IP: ").strip() 
    proto = input("Protocol (tcp/udp): ").strip().lower() 
    method = input("Mode (standard/reverse): ").strip().lower() 

    cmd = ( 
        ["iperf", "-c", ip, "-i", "1"] 
        + (["-u", "-b", "1000M"] if proto == "udp" else []) 
        + (["-R"] if method == "reverse" else []) 
    ) 
    log_file, tputs = f"log_{proto}_{ip}.txt", [] 

    print(f"\nGenerated iperf command: {' '.join(cmd)}")
    print(f"Running 10 tests... Logs will be saved to {log_file}\n") 

    for i in range(1, 11): 
        try: 
            out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout 

            with open(log_file, "a") as f: 
                f.write(f"--- Test {i} of 10 ---\n{out}\n") 

            match = re.search( 
                r"0\.0+-10\.\d+\s+sec.*?\s+(\d+(?:\.\d+)?)\s+[M|G]bits/sec", out 
            ) 
            if match: 
                tputs.append(float(match.group(1))) 
            
            print(f"Completed Test {i}/10") 

        except Exception as e: 
            sys.exit(f"Fatal Error: {e}") 

        time.sleep(1) 

    if tputs: 
        stats_text = (
            "\n--- STATISTICAL RESULTS (Mbits/sec) ---\n"
            f"Avg: {statistics.mean(tputs):.2f} | "
            f"Min: {min(tputs):.2f} | "
            f"Max: {max(tputs):.2f} | "
            f"StdDev: {(statistics.stdev(tputs) if len(tputs)>1 else 0):.2f}\n"
        )
        
        print(stats_text) 
        
        with open(log_file, "a") as f:
            f.write(stats_text)

if __name__ == "__main__": 
    main()