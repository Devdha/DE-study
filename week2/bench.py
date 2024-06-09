import boto3
import time

class StorageBenchmark:
    def __init__(self, local_file):
        self.local_file = local_file

    def run_benchmark(self):
        raise NotImplementedError("Subclasses should implement this method")

    def calculate_average(self, times):
        return sum(times) / len(times)

class S3Benchmark(StorageBenchmark):
    def __init__(self, local_file, bucket_name, key):
        super().__init__(local_file)
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name
        self.key = key

    def run_benchmark(self):
        upload_times = []
        download_times = []

        for _ in range(100):
            start_time = time.time()
            self.s3.upload_file(self.local_file, self.bucket_name, self.key)
            upload_times.append(time.time() - start_time)
            
            start_time = time.time()
            self.s3.download_file(self.bucket_name, self.key, self.local_file)
            download_times.append(time.time() - start_time)

        avg_upload_time = self.calculate_average(upload_times)
        avg_download_time = self.calculate_average(download_times)
        print(f"S3 Average Upload Time: {avg_upload_time} seconds")
        print(f"S3 Average Download Time: {avg_download_time} seconds")

class EFSBenchmark(StorageBenchmark):
    def __init__(self, local_file, efs_path):
        super().__init__(local_file)
        self.efs_path = efs_path

    def run_benchmark(self):
        upload_times = []
        download_times = []

        for _ in range(100):
            
            start_time = time.time()
            with open(self.local_file, 'rb') as src_file:
                with open(self.efs_path, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            upload_times.append(time.time() - start_time)
            
            start_time = time.time()
            with open(self.efs_path, 'rb') as src_file:
                with open(self.local_file, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            download_times.append(time.time() - start_time)

        avg_upload_time = self.calculate_average(upload_times)
        avg_download_time = self.calculate_average(download_times)
        print(f"EFS Average Upload Time: {avg_upload_time} seconds")
        print(f"EFS Average Download Time: {avg_download_time} seconds")

class EBSBenchmark(StorageBenchmark):
    def __init__(self, local_file, ebs_path):
        super().__init__(local_file)
        self.ebs_path = ebs_path

    def run_benchmark(self):
        upload_times = []
        download_times = []

        for _ in range(100):
            
            start_time = time.time()
            with open(self.local_file, 'rb') as src_file:
                with open(self.ebs_path, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            upload_times.append(time.time() - start_time)
            
            start_time = time.time()
            with open(self.ebs_path, 'rb') as src_file:
                with open(self.local_file, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            download_times.append(time.time() - start_time)

        avg_upload_time = self.calculate_average(upload_times)
        avg_download_time = self.calculate_average(download_times)
        print(f"EBS Average Upload Time: {avg_upload_time} seconds")
        print(f"EBS Average Download Time: {avg_download_time} seconds")

def main():
    local_file = 'submission.csv'
    s3_benchmark = S3Benchmark(local_file, 'hasan-donghun', 'submission.csv')
    efs_benchmark = EFSBenchmark(local_file, '../submission.csv')
    ebs_benchmark = EBSBenchmark(local_file, '../submission.csv')

    print("Starting S3 Benchmark...")
    s3_benchmark.run_benchmark()
    print("\nStarting EFS Benchmark...")
    efs_benchmark.run_benchmark()
    print("\nStarting EBS Benchmark...")
    ebs_benchmark.run_benchmark()

if __name__ == "__main__":
    main()

