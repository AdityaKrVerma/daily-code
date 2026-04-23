class DatabaseSession:
    def __enter__(self):
        print("Connecting...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection.")

with DatabaseSession():
    print("Doing work...")