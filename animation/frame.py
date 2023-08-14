from animation import constants as c

class Frame:
    def __init__(self, frameNumber, keyType, easeType=None, easeVal=None, motionID=None, spacingCount=None, steps=1):
        self._validate_frame_number(frameNumber)
        self._validate_key_type(keyType)
        self._validate_ease_type(easeType)
        self._validate_motion_id(motionID)
        self._validate_spacing_count(spacingCount)

        self.frameNumber = frameNumber
        self.keyType = keyType
        self.easeType = easeType
        self.motionID = motionID
        self.spacingCount = spacingCount

        # doesn't have validation yet
        self.easeVal = easeVal
        self.steps = steps

    def _validate_frame_number(self, frameNumber):
        if not isinstance(frameNumber, int):
            raise TypeError("frameNumber must be an integer.")

    def _validate_key_type(self, keyType):
        if keyType not in c.KEYTYPES:
            raise ValueError(f"Invalid keyType. Allowed values: {c.KEYTYPES}")

    def _validate_motion_id(self, motionID):
        if motionID is not None and not isinstance(motionID, int):
            raise TypeError("motionID must be an integer.")

    def _validate_spacing_count(self, spacingCount):
        if spacingCount is not None and not isinstance(spacingCount, int):
            raise TypeError("spacingCount must be an integer.")

    def _validate_ease_type(self, easeType):
        if easeType is not None and easeType not in c.EASETYPES:
            raise ValueError(f"Invalid easeType. Allowed values: {c.EASETYPES}")
