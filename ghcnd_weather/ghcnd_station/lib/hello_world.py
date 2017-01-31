import parsekit


class SayHello(parsekit.Step):

    def run(self, input_, metadata):
        self.log.info("Hello, world!")
        return input_, metadata