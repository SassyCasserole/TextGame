class PriorityDisplayQueue:

    def __init__(self, new_entry):
        self._entries = [new_entry]

    def add(self, new_entry):
        if not self._entries:
            self._entries.append(new_entry)
        else:
            if new_entry.text:
                for i, entry in enumerate(self._entries):
                    if new_entry.priority <= entry.priority:
                        self._entries.insert(i, new_entry)
                        break

    def reset(self):
        self._entries = []

    def highest(self):
        return self._entries[0]

    def lowest(self):
        return self._entries[-1]

    def __getitem__(self, item):
        return self._entries[item]

    def __repr__(self):
        return str([entry for entry in self._entries])