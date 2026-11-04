from typing import TypedDict, NotRequired, Required

class ResearchReport(TypedDict):
    Executive_Summary: str
    Research_Methodology: str
    Topic_Overview: str
    Key_Findings: str
    Comparative_Analysis: str
    Opportunities_and_Benefits: str
    Risks_and_Challenges: str
    Emerging_Trends: str
    Future_Outlook: str
    Confidence_Assessment: str
    Conclusion: str
    Actionable_Insights_and_Recommendations: str

class InputState(TypedDict):
    topic: Required[str]
    source_credibility_criteria: Required[str]
    report_tone_and_style_guidelines: Required[str]
    data_privacy_and_compliance_details: Required[str]
    actionable_insights_format: Required[str]
    topic_scope_and_exclusions: Required[str]

class OutputState(TypedDict):
    research_report: Required[ResearchReport]
    status: Required[str]
    ResearchReportAgent_route: Required[str]

class State(InputState, OutputState, total=False):
    pass
INPUT_FIELDS = ('topic', 'source_credibility_criteria', 'report_tone_and_style_guidelines', 'data_privacy_and_compliance_details', 'actionable_insights_format', 'topic_scope_and_exclusions')
REQUIRED_INPUT_FIELDS = ('topic', 'source_credibility_criteria', 'report_tone_and_style_guidelines', 'data_privacy_and_compliance_details', 'actionable_insights_format', 'topic_scope_and_exclusions')
OUTPUT_FIELDS = ('research_report', 'status', 'ResearchReportAgent_route')
_STATE_DEFAULTS = {'status': 'failure', 'ResearchReportAgent_route': 'failure'}

def state_defaults() -> dict:
    return _STATE_DEFAULTS.copy()
InputState.__required_keys__ = frozenset(['actionable_insights_format', 'data_privacy_and_compliance_details', 'report_tone_and_style_guidelines', 'source_credibility_criteria', 'topic', 'topic_scope_and_exclusions'])
InputState.__optional_keys__ = frozenset([])
OutputState.__required_keys__ = frozenset(['ResearchReportAgent_route', 'research_report', 'status'])
OutputState.__optional_keys__ = frozenset([])
