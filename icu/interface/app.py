from multiapp import MultiApp

from apps import metrics, real_time


app = MultiApp()


app.add_app("Real time", real_time.app)
app.add_app("Metrics", metrics.app)

app.run()