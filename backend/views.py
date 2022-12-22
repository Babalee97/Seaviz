import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.core.cache import cache, caches
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import VisualsSerializer
from .models import Visual, DataLoad
from .forms import DataLoadingForm

plt.switch_backend('agg')

plotters = {
    'box'   : sns.boxplot,
    'bar'   : sns.barplot,
    'count' : sns.countplot,
    'boxen' : sns.boxenplot,
    'swarm' : sns.swarmplot,
    'violin': sns.violinplot,
    'point' : sns.pointplot,
    'strip' : sns.stripplot
}

class DataLoadingView(View):
    form_class = DataLoadingForm
    template_name = 'backend/dataload_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(None)
        filename = request.FILES['data']
        userid = request.POST['userid']
        cache.set(userid, pd.read_csv(filename))
        return render(request, self.template_name, {'form':form})


class PlottingView(APIView):

    def get(self, request):
        # userdata = cache.get(request.POST['userid'])
        # plot_type = request.POST['plot_type']
        # plotters['plot_type'](request.POST minus userid & plot_type)
        # save_name = '{}_{}.png'.format(userid, plot_type)
        # plt.savefig('media/save_name')

        # viz = Visual()
        # viz.plot_image = 'save_name'
        # viz.plot_type = 'plot_type'

        plotters['boxen'](data=cache.get('user2'))
        plt.savefig('media/boxplot.png')

        viz = Visual()
        viz.plot_image = 'boxplot.png'
        viz.plot_type = 'boxplot'

        serializer = VisualsSerializer(viz)
        return Response(serializer.data)

def clear_user_data(request):
    cache.delete('user1')
    return HttpResponse()
    

    

        












