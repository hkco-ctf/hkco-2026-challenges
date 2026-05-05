import random, time, requests
from shapely.geometry import LineString
from tqdm import tqdm

OVERPASS_ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.osm.ch/api/interpreter",
]
HEADERS = {"User-Agent": "street-point-sampler/1.0"}
                                                                                                                                                                                                                                                                                                                                                                                                                                 
street_map = {
    "1": "Tai Yau Street",
    "2": "Sheung Hei Street",
    "3": "Sam Chuk Street",
    "4": "Sze Mei Street",
    "5": "Ng Fong Street",
    "6": "Luk Hop Street",
    "7": "Tsat Po Street",
    "8": "Pat Tat Street",
}

def overpass_query(q):
    last_err = None
    for url in OVERPASS_ENDPOINTS:
        for attempt in range(3):
            try:
                r = requests.post(url, data={"data": q}, headers=HEADERS, timeout=60)
            except requests.RequestException as e:
                last_err = e
                time.sleep(2)
                continue
            if r.status_code == 200 and r.text.lstrip().startswith("{"):
                return r.json()
            if r.status_code in (429, 504):
                time.sleep(5)
                continue
            last_err = RuntimeError(f"{url} -> HTTP {r.status_code}: {r.text[:200]}")
            break
    raise RuntimeError(f"Overpass failed: {last_err}")


SAN_PO_KONG_BBOX = (22.328, 114.193, 22.345, 114.210)  # s, w, n, e


def generate_points(area, street, n_points):
    s, w, n, e = SAN_PO_KONG_BBOX
    q = f"""
    [out:json][timeout:60];
    way[highway]["name:en"="{street}"]({s},{w},{n},{e});
    out geom;
    """
    ways = overpass_query(q)["elements"]
    if not ways:
        raise RuntimeError(f"No ways found for street={street!r} in {area}")

    lines, lengths = [], []
    for w in ways:
        coords = [(p["lon"], p["lat"]) for p in w["geometry"]]
        line = LineString(coords)
        lines.append(line)
        lengths.append(line.length)

    total = sum(lengths)
    probs = [L / total for L in lengths]

    res = []
    for _ in range(n_points):
        line = random.choices(lines, weights=probs, k=1)[0]
        p = line.interpolate(random.random(), normalized=True)
        res.append(f"({p.y:.6f}, {p.x:.6f})")
    return res

flag = 'fun_s7r33t5!'

def main():
    # Convert the flag to bytes
    flag_bytes = flag.encode()
    # Convert the bytes to an integer
    num = int.from_bytes(flag_bytes, 'big')
    # Convert the integer to a base-8 string
    enc = oct(num)[2:]  # Remove the '0o' prefix
    # Make the digits 1-8 instead of 0-7
    enc = ''.join(str(int(c) + 1) for c in enc)
    print('Flag:', enc)

    # Print count of each digit in the encrypted flag
    from collections import Counter
    digit_counts = dict(Counter(enc))
    
    points_map = {}
    # Generate random points on the streets based on the digit counts
    for digit, count in tqdm(digit_counts.items()):
        street = street_map[digit]
        points = generate_points("San Po Kong", street, count)
        points_map[digit] = points

    # Map each point back to the corresponding digit in the encrypted flag, randomly without replacement
    final_points = []
    for digit in enc:
        point = random.choice(points_map[digit])
        final_points.append(point)
        points_map[digit].remove(point)
    
    # Write the final points to a file
    with open("geoguesser.txt", "w") as f:
        for point in final_points:
            f.write(f"{point}\n")

if __name__ == "__main__":
    main()