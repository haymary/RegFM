from src.analysis.Analyzer import Analyzer


class EventAnalyzer():
    def get_event_types(self, event_tags):
        return Analyzer().analyze_skills(event_tags)