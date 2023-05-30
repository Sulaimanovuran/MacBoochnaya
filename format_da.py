
import math
import re

def format_desc_pro(text):


    cpu_regex = re.compile(r"CPU.*?(\d+)core")

    gpu_regex = re.compile(r"Graphics.*?(\d+)core")

    chip_version = re.search(r"(?<=M[12] )\w+", text).group(0)

    match = re.search(r'Color\s+(\w+)', text)
    
    chip_pattern = r"\bM[1-2]\b"

    chip_match = re.search(chip_pattern, text)

    if match:
        chip = chip_match.group(0)
    else:
        chip = '?'

    if match:
        color = match.group(1)
        if color == 'Gray':
            color = 'Space Gray'
        
    else:
        color = "?"

    pattern = r'(\d+\.\d+)\s*inches'

    match = re.search(pattern, text)

    if match:
        resolution = round(float(match.group(1)))
        
    else:
        resolution = '?'


    cpu_cores = cpu_regex.search(text)
    if cpu_cores:
        cpu_cores = cpu_cores.group(1)
    else:
        cpu_cores = "?"

    gpu_cores = gpu_regex.search(text)
    if gpu_cores:
        gpu_cores = gpu_cores.group(1)
    else:
        gpu_cores = "?"

    return {'resolution': resolution, 'chip': chip, 'c_version': chip_version, 'cpu':cpu_cores, 'gpu': gpu_cores, 'color': color}











def format_desc_air(text):

    if "M1 " not in text and "M2 " not in text:
        return None
    

    pre_version = re.search(r"macbook\s+(air|pro)", text.lower(), re.IGNORECASE)
    if pre_version:
        m_version = pre_version.group(1).title()

    cpu_cores = None
    if m_version.lower() == 'air':
        cpu_regex = r"CPU .*?((Octa)?core|2core|4core)"
        cpu_match = re.search(cpu_regex, text)
        if cpu_match:
            cpu_str = cpu_match.group(1)
            if "Octa" in cpu_str:
                cpu_cores = 8
            elif "2core" in cpu_str:
                cpu_cores = 2
            elif "4core" in cpu_str:
                cpu_cores = 4
        else:
            cpu_cores = None
    else:
        cpu_regex = re.compile(r"CPU.*?(\d+)core")
        cpu_cores = cpu_regex.search(text)
        if cpu_cores:
            cpu_cores = cpu_cores.group(1)
        else:
            cpu_cores = "?"


    gpu_regex = re.compile(r"Graphics.*?(\d+)core")
    gpu_cores = gpu_regex.search(text.lower())

    if gpu_cores:
        gpu_cores = gpu_cores.group(1)
    else:
        gpu_cores = "?"

    try:
        chip_version = re.search(r"(?<=M[12] )\w+", text).group(0)
        if 'Pro' not in chip_version and 'Max' not in chip_version:
            chip_version = ''
    except: 
        chip_version = ''

    c_match = re.search(r'Color\s+(\w+)', text)
    if c_match:
        color = c_match.group(1)

        if color == 'Gray':
            color = 'Space Gray'
        
    else:
        color = "?"


    chip_pattern = r"\bM[1-2]\b"

    chip_match = re.search(chip_pattern, text)

    if chip_match:
        chip = chip_match.group(0)
    else:
        chip = '?'

    

    pattern = r'(\d+\.\d+)\s*inches'

    r_match = re.search(pattern, text)

    if r_match:
        resolution = math.floor(float(r_match.group(1)))
        
    else:
        resolution = '?'
    
    if resolution < 14 and m_version == 'Pro':
        if chip == 'M1':
            cpu_cores = 8
            gpu_cores = 8
        elif chip == 'M2':
            cpu_cores = 8
            gpu_cores = 10

    return {'m_version': m_version, 'resolution': resolution, 'chip': chip, 'c_version': chip_version, 'cpu':cpu_cores, 'gpu': gpu_cores, 'color': color}



# print(format_desc_air('Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 7‑Core GPU'))
# import re

lst = ["KRW 2,441,000 More price information 1st place 16GB, SSD 512GB", 
       "KRW 3,358,000 More price information 32GB, SSD 1TB", 
       "KRW 4,896,000 More price information 38core GPU, 64GB, SSD 1TB", 
       "Temporary out of stock 32GB, SSD 2TB",
       "KRW 4,240,800 More price information 2nd place 38core GPU, 32GB , SSD 1TB"]

# for i in lst:
#     m = re.search(r"(\d+)core", i)
#     if m:
#         gpu = m.group(1)
#         print(m)
#     else:
#         print(m)


# for item in lst:
#     ram = re.findall(r'(\d+)GB', item)[0]
#     storage = re.findall(r'SSD (\d+TB|\d+GB)', item)[0]
#     print(f"RAM: {ram}, Storage: {storage}")