from latest_ai_development.graph.state import State


class ResearchReportAgent:
    """Agent performs autonomous comprehensive research and generates the structured research report with all required sections, respecting data privacy and compliance constraints."""

    def build(self):
        return dict(
            agent_name="ResearchReportAgent",
            input_fields=[
                "topic",
                "source_credibility_criteria",
                "report_tone_and_style_guidelines",
                "data_privacy_and_compliance_details",
                "actionable_insights_format",
                "topic_scope_and_exclusions",
            ],
            output_fields=["research_report", "status", "ResearchReportAgent_route"],
            is_conditional=True,
            routing_rules={"success": "TerminalSuccess", "failure": "TerminalFailure"},
            structured_output=True,
        )


class TerminalSuccessResponder:
    """Terminal node for successful report generation, outputs the final research report and status."""

    def build(self):
        return dict(
            agent_name="TerminalSuccessResponder",
            input_fields=["research_report", "status"],
            output_fields=["research_report", "status"],
            is_conditional=False,
            structured_output=True,
        )


class TerminalFailureResponder:
    """Terminal node for failure in report generation, outputs failure status and empty report."""

    def build(self):
        return dict(
            agent_name="TerminalFailureResponder",
            input_fields=["status"],
            output_fields=["research_report", "status"],
            is_conditional=False,
            structured_output=True,
        )

NODE_REGISTRY: dict = {}
ROUTER_REGISTRY: dict = {}
