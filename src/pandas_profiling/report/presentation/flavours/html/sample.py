from pandas_profiling.report.presentation.core.sample import Sample
from pandas_profiling.report.presentation.flavours.html import templates


class HTMLSample(Sample):
    def render(self):
        self.content["sample"] = self.content["sample"].to_html(
            classes="sample table table-striped"
        )
        return templates.template("sample.html").render(**self.content)
