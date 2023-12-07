# https://qiita.com/maebaru/items/579afe3c30edc143968d

class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def push(self, x: int) -> None:
        self.inputStack.append(x)

    def pop(self) -> int:
        self.moveInputToOutput()
        return self.outputStack.pop()

    def peek(self) -> int:
        self.moveInputToOutput()
        return self.outputStack[-1]

    def empty(self) -> bool:
        return not self.inputStack and not self.outputStack

    # moveInputToOutput is a helper function that moves all elements from inputStack to outputStack if outputStack is empty
    def moveInputToOutput(self):
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
