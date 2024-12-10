from .power_assessment import PowerAssessment
from .proximity_evaluation import ProximityEvaluation

# Class comment
class LeaderSelection:
    def __init__(self):
        self.power_assessment = PowerAssessment()
        self.proximity_evaluation = ProximityEvaluation()


    def update(self, hub):
        # Update the leader robots based on power level
        self.power_assessment.update(hub)

        # No implemented yet -> factor in proximity to interesting locations in leaer selection
        # self.proximity_evaluation.update()