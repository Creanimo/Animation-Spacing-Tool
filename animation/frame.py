import constants as c

class frame:
    def __init__(self, frameNumber, keyType, easetype = None, easeVal = None, motionID = None, spacingCount = None):
        if not isinstance(frameNumber, int):
            raise TypeError("Frame Number must be a whole number.")
        self.number = number

        if not keyType in c.KEYTYPES:
            raise TypeError(f"Key Type must be one of these: {c.KEYTYPES}.")
        self.keyType = keyType

        self.motionID = motionID
        # for keys, extreme, anticipation, overshoot and breakdowns.
        self.easetype = easetype  # defines distribution of inbetween spacings from one to another.
        # for inbetweens
        self.easeVal = easeVal # percentage of easing (for inbetweens only)
        self.spacingCount = spacingCount # the number of the current division between keys