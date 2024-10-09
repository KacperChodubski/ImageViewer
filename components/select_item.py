class SelectItem:
    def __init__(self, label, function) -> None:
        self.label = label
        self.function = function

    def __str__(self) -> str:
        return self.label

    def call(self):
        self.function()
