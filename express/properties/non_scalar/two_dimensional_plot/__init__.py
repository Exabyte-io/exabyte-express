from express.properties.non_scalar import NonScalarProperty


class TwoDimensionalPlotProperty(NonScalarProperty):
    """
    Base 2D-plot property class.
    """

    def __init__(self, name, parser, *args, **kwargs):
        super(TwoDimensionalPlotProperty, self).__init__(name, parser, *args, **kwargs)
        self.legend = None
        self.xDataArray = None
        self.yDataSeries = None

    def _serialize(self):
        serialized_data = {
            'name': self.name,
            'xAxis': self.esse.get_schema_default_values(self.name)["xAxis"],
            'yAxis': self.esse.get_schema_default_values(self.name)["yAxis"],
            'xDataArray': self.xDataArray,
            'yDataSeries': self.yDataSeries,
        }
        if self.legend:
            serialized_data.update({"legend": self.legend})
        return serialized_data
