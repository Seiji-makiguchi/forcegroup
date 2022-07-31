import os.path
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
sys.path.append(str(Path(__file__).resolve().parent.parent))
from django.shortcuts import render
from django.views.generic import TemplateView
import glob
from mononofu import settings


# Create your views here.
class TopPageView(TemplateView):
    template_name = "top.html"

    def get(self, request, *args, **kwargs):
        context = super(TopPageView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)


class TakashibaView(TemplateView):
    template_name = "takashiba.html"

    def get(self, request, *args, **kwargs):
        print(settings.STATIC_DIR.format("ero*png"))
        img_path_list = glob.glob(settings.STATIC_DIR.format("img/ero*png"))
        context = super(TakashibaView, self).get_context_data(**kwargs)
        print(img_path_list)
        context["img_list"] = [f"img/{os.path.basename(k)}" for k in img_path_list]
        return render(self.request, self.template_name, context)
