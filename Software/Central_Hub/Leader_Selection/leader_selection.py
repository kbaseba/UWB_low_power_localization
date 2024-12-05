from .power_assessment import PowerAssessment
from .proximity_evaluation import ProximityEvaluation

# Class comment
class LeaderSelection:
    def __init__(self):
        self.power_assessment = PowerAssessment()
        self.proximity_evaluation = ProximityEvaluation()


    def update(self, robots):
        # Update the leader robots based on power level
        leader_nodes = self.power_assessment.update(robots)

        # No implemented yet -> factor in proximity to interesting locations in leaer selection
        self.proximity_evaluation.update()

        return leader_nodes
