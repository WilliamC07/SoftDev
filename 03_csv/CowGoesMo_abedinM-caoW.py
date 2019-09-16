import random

def get_model_information():
    file_name = "occupations.csv"
    raw_lines = open(file_name).readlines()
    raw_lines = raw_lines[1:-1]  # removes header and total rows
    
    job = []  # Percent of Management is 6.1, so there will be 61 "Management" in the list
    for csv_line in raw_lines:
        title_percent_tuple = process_csv_line(csv_line) 
        for _ in range(title_percent_tuple[1]):
            job.append(title_percent_tuple[0])

    return job 

def process_csv_line(line):
    # remove end of line character
    line = line[:-1]

    # each line may or may not have a quote
    if '"' in line:
        data = line.split('",');
        title = data[0][1:-1]  # remove leading quote
        return (title, int(float(data[1])) * 10) # store percent as whole number
    else:
        data = line.split(',')
        title = data[0]
        return (title, int(float(data[1])) * 10)


def choose_random_job():
    job = get_model_information()
    return random.choice(job) 


if __name__ == "__main__":
    print(choose_random_job())

