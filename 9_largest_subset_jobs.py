def largest_subset_jobs(jobs):
	sorted_jobs = sorted(jobs, key=lambda x : x[1])
	# print(f"sorted: {sorted_jobs}")
	results = []
	for job in sorted_jobs:
		if not results:
			# print("congrats")
			results.append(job)
		if job[0]>=results[-1][1]: 
			print("job: ",job)
			print(job[0], results[-1][1])
			results.append(job)
	return results

jobs = [(0,6), (1,4), (3,5), (3,8), (4,7), (5,9), (6,10), (8,11)]
print(largest_subset_jobs(jobs))