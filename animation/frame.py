from animation import constants as c

class Frame:
    def __init__(self, frameNumber, keyType, easeType = None, easeVal = None, motionID = None, spacingCount = None):
        if not isinstance(frameNumber, int):
            raise TypeError("Frame Number must be a whole number.")
        self.frameNumber = frameNumber

        if not keyType in c.KEYTYPES:
            raise TypeError(f"Key Type must be one of these: {c.KEYTYPES}.")
        self.keyType = keyType

        if not isinstance(motionID, int):
            raise TypeError("Motion ID must be a whole number.")
        self.motionID = motionID

        # Some keys
        if not keyType in c.KEYTYPES:
            raise TypeError(f"Ease Type must be one of these: {c.EASETYPES}.")
        self.easeType = easeType  # defines distribution of inbetween spacings from one to another.

        self.spacingCount = spacingCount # the number of the current division between keys

        # for inbetweens
        self.easeVal = easeVal # percentage of easing (for inbetweens only)