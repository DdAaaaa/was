from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import QuarterBlock


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def quarter_block(request):
    """
    quarter block request를 받아서 model을 업데이트 해주는 view
    request.POST의 형식
    ex)
    `name`: username
    timeslots: {[
        `level`: int
        `time`: datetime
        ]}

    :param request:
    :return:
    """
    if request.method == 'POST':
        infos = request.POST
        username = infos.get('name')
        user = User.objects.get(username=username)
        timeslots = infos.get('timeslots')
        try:
            for level, time in timeslots.items():
                target_block = QuarterBlock.objects.create(user=user, level=level, action_time=time)
                target_block.save()
        except Exception as e:
            # ToDo. if save failed, Row can be duplicated
            resp = HttpResponse("DB insert failed")
            resp.status_code = 500
            return resp
        return HttpResponse("Done")

    elif request.method == 'GET':
        return HttpResponse("테스트 페이지입니다.")
    else:
        resp = HttpResponse("bad request")
        resp.status_code = 404
        return resp
