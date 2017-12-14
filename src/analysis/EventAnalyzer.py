from src.analysis.Analyzer import Analyzer


class EventAnalyzer():
    def get_event_types(self, event_tags):
        """
        Returns the category of the event according to tags
        :param event_tags: list of event tags
        :return: list of ints
        """
        return Analyzer().analyze_skills(event_tags)