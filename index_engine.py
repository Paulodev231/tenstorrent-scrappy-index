import os
import csv
from datetime import datetime

# Logic: Identify engineering-led startups hitting GPU cost/scaling walls
KEYWORDS = ["CUDA", "HPC", "NVIDIA", "H100", "Low-level", "Kernel", "RISC-V"]

def generate_gtm_report(matches):
    """Saves identified technical leads for Tenstorrent outreach."""
    if not matches: return
    filename = "tenstorrent_discovery_list.csv"
    keys = matches[0].keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(matches)

def simulate_discovery():
    """Simulates scanning technical job boards for hardware bottlenecks."""
    # Example data representing the 'scrappy teams' Tenstorrent targets
    raw_data = [
        {"company": "DeepCompute AI", "desc": "Scaling LLMs on H100 clusters. Need CUDA optimization.", "site": "deepcompute.ai"},
        {"company": "VectorFlow", "desc": "Building custom AI kernels. Exploring RISC-V for on-prem efficiency.", "site": "vectorflow.io"}
    ]
    
    qualified_leads = []
    for entry in raw_data:
        signals = [k for k in KEYWORDS if k.lower() in entry['desc'].lower()]
        if signals:
            qualified_leads.append({
                "Company": entry['company'],
                "Pain_Signals": ", ".join(signals),
                "Source_URL": entry['site'],
                "Discovery_Date": datetime.now().strftime("%Y-%m-%d")
            })
    
    generate_gtm_report(qualified_leads)
    print("Success: Tenstorrent GTM Discovery Report Generated.")

if __name__ == "__main__":
    simulate_discovery()
