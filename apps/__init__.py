from flask import Flask
from apps.views import testview, basicFuncViews, histogramViews, segmentationViews, smoothSharpenViews, repairViews, \
    morphologicalViews
from apps.views import filesViews

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(testview.app)
app.register_blueprint(filesViews.app)
app.register_blueprint(basicFuncViews.app)
app.register_blueprint(histogramViews.app)
app.register_blueprint(segmentationViews.app)
app.register_blueprint(smoothSharpenViews.app)
app.register_blueprint(morphologicalViews.app)
app.register_blueprint(repairViews.app)
