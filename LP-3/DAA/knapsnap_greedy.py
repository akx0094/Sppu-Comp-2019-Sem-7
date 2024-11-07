class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Initialize the result and free time slots
    result = [None] * n  # To store result (sequence of jobs)
    slot = [False] * n   # To keep track of free time slots

    # Iterate through all jobs
    for job in jobs:
        # Find a free slot for this job (from min(job.deadline, n)-1 to 0)
        for j in range(min(job.deadline, n) - 1, -1, -1):
            if not slot[j]:  # If the slot is free
                slot[j] = True  # Mark this slot as occupied
                result[j] = job.id  # Assign the job to this slot
                break

    # Print the result
    print("Scheduled Jobs: ", end="")
    for job in result:
        if job is not None:
            print(job, end=" ")
    print()

def main():
    # Example jobs (id, deadline, profit)
    jobs = [
        Job('a', 2, 100),
        Job('b', 1, 19),
        Job('c', 2, 27),
        Job('d', 1, 25),
        Job('e', 3, 15)
    ]

    n = len(jobs)
    job_sequencing(jobs, n)

if __name__ == "__main__":
    main()
