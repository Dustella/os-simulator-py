class MemoryManager:
    def __init__(self, total_memory_pages=24):
        self.total_memory_pages = total_memory_pages
        self.memory = [None] * total_memory_pages
        self.next_fit_pointer = 0  # Pointer for next fit algorithm

    def allocate(self, num_pages):
        start_page = self.next_fit_pointer
        end_page = start_page

        for _ in range(self.total_memory_pages):
            if self.memory[end_page % self.total_memory_pages] is None:
                end_page += 1
                if end_page - start_page == num_pages:
                    # Found a suitable block
                    for page in range(start_page, end_page):
                        self.memory[page %
                                    self.total_memory_pages] = "Occupied"
                    self.next_fit_pointer = end_page % self.total_memory_pages
                    return start_page
            else:
                # Reset start_page and end_page if the current page is occupied
                end_page += 1
                start_page = end_page

        return -1  # Allocation failed

    def free(self, start_page, num_pages):
        for page in range(start_page, start_page + num_pages):
            self.memory[page % self.total_memory_pages] = None

    def get_usage(self):
        # Calculate the number of used pages
        return self.memory
