""""
    модуль views.py
    Содержит представления для реализаии проекта AlchTaskTree

    VCreateTask(request) - функция представления, вызывающая форму Django (class CreateTask),
    для создания новой записи задачи (Tasks).
    Передает в таблицу Tasks поля Текст задачи (title), Дата начала выполнения задачи Start,
    Дата завершения задачи End.

    VCreateContact(request) - функция, вызывающая форму Django (class CreateContact), для создания новой
    записи в таблице Контакты (Contacts).
    Передает в таблицу Contacts поля Фамилия - last_name, Имя - first_name, Отчество - second_name.

    MainPage(request) - функция, вызывающая html шаблон, для главной страницы проекта.
    Страница вызывает список задач, рядом с заголовком задачи реализованы кнопки для удаления и редактирования задачи.
    Также реализованы кнопки связывания задачи с другими задачами и кнопка связывания задачи с контактами.
    Заголовки задач реализованы в виде ссылок на карточку для редактирования конкретной задачи.
    Страница содержит поиск задачи по введенному пользователем контексту.

    PageContacts(request) - функция, вызывающая html шаблон, для страницы со списком контактов (Contacts).
    Страница содержит поиск контакта по введенной пользователем фамилии, кнопку для создания новгго контакта.
    Реализованы кнопка удаления выбранного контакта. ФИО контакта реализованы, как ссылки на страницу
    редактирования данных выборанного контакта.

    VCardContact(request, contact_id) - функция, вызывающая html шаблон, для страницы редактирования данных конаткта.
    Атрибут contact_id - значение ключевого поля id таблицы контактов.

    VEditTask(request, task_id)  - функция, вызывающая html шаблон, для страницы редактирования данных задачи.
    Редактирование связей задач между собой и с контактами осуществляется в других функциях.
    Атрибут task_id - значение ключевого поля id таблицы задач.

    VCardTask(request, task_id) - функция, вызывающая html шаблон, для страницы редактирования
    данных о взаимсвязях задач между собой.
    Атрибут task_id - значение ключевого поля id таблицы задач.
    Страница содержит список связанных с данной задачей других задач той же таблицы.
    Это аналог исходящих стрелок связи задач, от выбранной к указанным в списке.
    Рядом с заголовком связанной задачи реализована кнопка удаления связи задач из таблицы связей Univers_list.
    Страница содержит список задач, несвязанных с выбранной задачей. При этом исключается повторное связывание
    двух задач однонаправленной связью. В списке отсутствует выбранная задача, т.к. исключено связывание задачи
    самой с собой.
    Напротив заголовка каждой несвязанной задачи реализована кнопка добавления связи задач, через добавление
    соответствующей записи в таблицу Univers_list.
    Реализованы поиски связанной задачи по контексту в ее загаловке и аналогично по списку несвязанных задач.

    VContactsTask(request, task_id) - функция, вызывающая html шаблон, для страницы редактирования
    данных о взаимсвязях задачи с контактами, а также ролевым значение этой взаимосвязи.
    Атрибут task_id - значение ключевого поля id таблицы задач.
    Страница содержит список связанных с данной задачей контактов и ролей взаимосвязи.
    Это аналог исходящих стрелок связи задач, от выбранной к указанным в списке конатктам.
    Рядом с заголовком связанного контакта  реализована кнопка удаления связи задачи и контакта
    из таблицы связей Univers_list.
    Там же реализован выпадающий список ролей взаимосвязи задачи и контакта (исполнитель, руководитель и т.п.) для
    выбора роли для данной взаимосвязи. Рядом с данным выпадающим списком реализована кнопка сохранения данных о роли
    в поле Role таблицы Univers_list.
    Страница содержит список всех контактов. При этом не исключается повторное связывание
    задач и контакта.

    Напротив заголовка каждого несвязанного с задачей контакта  реализована кнопка добавления связи задачи и контакта,
    через добавление соответствующей записи в таблицу Univers_list.
    Реализованы поиски связанных контактов задачи по контексту фамилии в ее загаловке
    и аналогично по списку несвязанных контактов.

"""
import uuid

from django.http import HttpResponse
from .forms import *
from sqlalchemy import *
from .backend.db import SessionLocal, DBSession
from django.shortcuts import render
from .models import *
from sqlalchemy.orm import *
from datetime import datetime
db = DBSession
# Base.metadata.create_all(engine)
# db = get_db()
def VCreateTask(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task_start = form.cleaned_data['start']
            task_end = form.cleaned_data['end']
            # Tasks.objects.create(title=title, start=task_start, end=task_end)
            VTask = Tasks(title=title, start=task_start, end=task_end) #id auto?
            db.add(VTask)
            db.commit()

    else:
        form = CreateTask()
    cont_form={'form': form}
    return render(request, 'create_contact.html',context=cont_form)
# Create your views here.
def VCreateContact(request):
    if request.method == 'POST':
        form = CreateContact(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            # Contacts.objects.create(last_name=last_name,first_name=first_name,second_name=second_name)
            VContact = Contacts(last_name=last_name,first_name=first_name,second_name=second_name)
            db.add(VContact)
            db.commit()
    else:
        form = CreateContact()
    cont_form={'form': form}
    return render(request, 'create_contact.html',context=cont_form)
def MainPage(request):
    FindTitle = ''
    if request.method == 'POST':
        if request.POST.get('btn_find')=='new_find':
            FindTitle = request.POST.get('FindTitle')
        id_del = request.POST.get('btn_del')
        # print(id_del)
        if id_del:
            db.execute(delete(Tasks).where(Tasks.id == uuid.UUID(id_del)))
            # db.delete(Dtask)
            db.commit()
    # t = db.query(Tasks)
    # tasks_lst = db.query(Tasks).filter(Tasks.title.ilike(f'%{FindTitle}%'))
    tasks_lst = db.query(Tasks).filter(Tasks.title.ilike(f'%{FindTitle}%')).all()
    # for h in tasks_lst:
    #     print(h.start)
    # print('id=',tasks_lst[0].id,type(tasks_lst[0].id))
    count_tasks = len(tasks_lst)
    # count_tasks = db.query(func.count(Tasks.id)).filter(Tasks.title.ilike(f'%{FindTitle}%')).scalar()
    # count_tasks = tasks_lst.count()
    if count_tasks == 0:
        PageStr = 'Нет задач соответствующих условиям'
    elif count_tasks > 0:
        PageStr = f'Количество задач = {count_tasks}'
    info_main = {'PageTitle': PageStr, 'tasks_list': tasks_lst,
                 'count_tasks': count_tasks, 'FindTitle': FindTitle}
    return render(request, 'main.html', context=info_main)
def PageContacts(request):
    FindTitle = ''
    if request.method == 'POST':
        if request.POST.get('btn_find'):
            FindTitle = request.POST.get('FindTitle')
        id_del = request.POST.get('btn_del')
        # print(id_del)
        if id_del:
            # Contacts.objects.get(id=id_del).delete()
            DContact = db.query(Contacts).filter(Contacts.id == uuid.UUID(id_del)).all()
            # db.execute(delete(Contacts).where(Contacts.id == id_del))
            if DContact:
                db.delete(DContact[0])
                db.commit()

    # contacts_lst = Contacts.objects.filter(last_name__icontains=FindTitle)
    # count_contacts = contacts_lst.count()

    search = "%{}%".format(FindTitle)
    contacts_lst = db.query(Contacts).filter(Contacts.last_name.like(search)).all()
    # count_contacts = Tasks.query(func.count(Tasks.id)).scalar()
    count_contacts = len(contacts_lst)
    if count_contacts == 0:
        PageStr = 'Нет контактов, соответствующих поиску'
    elif count_contacts > 0:
        PageStr = f'Количество контактов = {count_contacts}'
    info_main = {'PageTitle': PageStr, 'contacts_lst': contacts_lst,
                 'count_contacts': count_contacts, 'FindTitle': FindTitle}
    return render(request, 'contacts.html', context=info_main)
def VCardContact(request, contact_id):

    VContact = db.query(Contacts).filter(Contacts.id == uuid.UUID(contact_id)).all()[0]
    # print(VContact)
    vlast_name = VContact.last_name
    vfirst_name = VContact.first_name
    vsecond_name = VContact.second_name
    if request.method == 'POST':
        # VContact.last_name = request.POST.get('last_name')
        # VContact.first_name = request.POST.get('first_name')
        # VContact.second_name = request.POST.get('second_name')
        # VContact.save()
        vlast_name = request.POST.get('last_name')
        vfirst_name = request.POST.get('first_name')
        vsecond_name = request.POST.get('second_name')
        # db.execute(update(Contacts).where(Contacts.id == contact_id).values(
        #     first_name=vfirst_name,
        #     last_name=vlast_name,
        #     second_name=vsecond_name
        # ))
        UpContact = db.query(Contacts).filter(Contacts.id == uuid.UUID(contact_id)).all()[0]
        UpContact.last_name = vlast_name
        UpContact.first_name = vfirst_name
        UpContact.second_name = vsecond_name
        db.commit()
    return render(request, 'card_contact.html', context={'contact': {'last_name': vlast_name,
                                                                     'first_name': vfirst_name,
                                                                     'second_name': vsecond_name}})

def VEditTask(request, task_id):
    VTask = db.query(Tasks).filter_by(id = uuid.UUID(task_id)).all()
    # for u in VTask:
    #     print('u=',u)
    # print('VTask=',VTask)
    vtitle = VTask[0].title
    vstart = VTask[0].start
    vend  = VTask[0].end

    if request.method == 'POST':
        vtitle = request.POST.get('task_title')
        vstart = request.POST.get('start')
        vend = request.POST.get('date_end')
        # db.execute(update(Tasks).where(Tasks.id == task_id).values(
        # title = vtitle,
        # print(type(vstart),vstart)
        # end = vend))
        UpTask = db.query(Tasks).filter(Tasks.id == uuid.UUID(task_id)).first()
        UpTask.title = vtitle
        UpTask.start = vstart
        if UpTask.start=='':
            UpTask.start = null()
        else:
            UpTask.start = datetime.strptime(vstart,'%Y-%m-%d')
        UpTask.end = vend
        if UpTask.end=='':
            UpTask.end = null()
        else:
            UpTask.end = datetime.strptime(vend,'%Y-%m-%d')
        db.commit()
        # print(request.POST.get('task_title'),request.POST.get('start'),request.POST.get('date_end'))
    else:
        if vstart:
            vstart = vstart.strftime('%Y-%m-%d')
        if vend:
            vend = vend.strftime('%Y-%m-%d')
    FTask = {'title': vtitle, 'start': vstart, 'end': vend }

    return render(request, 'edit_task.html', context={'task': FTask})

def VCardTask(request, task_id):
    # find_task = Tasks.objects.filter(id=task_id)
    # vtask_id, vtask_title, vtask_start, vtask_end = db.scalar(select(Tasks.id,Tasks.title, Tasks.start, Tasks.end).where(Tasks.id == task_id))
    VTask = db.query(Tasks).filter(Tasks.id == uuid.UUID(task_id)).all()[0]
    vtask_id = VTask.id
    vtask_title = VTask.title
    vtask_start  = VTask.start
    vtask_end = VTask.end
    count_link_tasks = 0
    count_unlink_tasks = 0
    FindTitleUnLink = ''
    FindTitle = ''

    if vtask_id:
        lst_field_task = {'task_id': vtask_id, 'task_title': vtask_title, 'task_start': vtask_start, 'task_end': vtask_end}
        # link_task = Univers_list.objects.filter(id_out=vtask_id)
        # link_task =  db.scalar(select(Univers_list).where(Univers_list.id_out == vtask_id))
        # count_fulllink_task = Univers_list.filter(Univers_list.id_out == vtask_id).query(
        #     func.count(Univers_list.id)).scalar()
        count_fulllink_task = len(db.query(Univers_list).filter(Univers_list.id_out == vtask_id).all())
        # print('count_fulllink_task=',count_fulllink_task)
        # count_fulllink_task = link_task.count()
        if request.method == 'POST':
            btn_find_unlink = request.POST.get('btn_find_unlink')
            if btn_find_unlink:
                FindTitleUnLink = request.POST.get('FindTitleUnlink')
                btn_find_unlink = None
            btn_find_tlink = request.POST.get('btn_find_tsklink')
            if btn_find_tlink:
                FindTitle = request.POST.get('FindTitle')
                btn_find_tlink = None
                # print('FindTitle=',FindTitle)
        search = "%{}%".format(FindTitle)
        search1 = "%{}%".format(FindTitleUnLink)
        if count_fulllink_task>0:
            flist_link_task = db.query(Tasks).join(Univers_list, Tasks.id == Univers_list.id_in)
            flist_link_task = flist_link_task.filter(Univers_list.id_out == vtask_id and Tasks.title.like(search))
            flist_link_task = flist_link_task.add_columns(Tasks.id,Tasks.title,Univers_list.id_num).all()
            # flist_link_task = flist_link_task.join(Univers_list, Tasks.id == Univers_list.id_in).all()
            # print('dict',flist_link_task[0].__dict__)
            # db.query(Tasks).

            notlist_link_task = db.query(Tasks).outerjoin(Univers_list, Tasks.id == Univers_list.id_in).filter( Tasks.id!=vtask_id, Univers_list.id_in == null(),Tasks.title.like(search)).all()
            count_link_tasks = len(flist_link_task)
        else:
            flist_link_task = None
            # notlist_link_task = db.query(Tasks).filter(Tasks.id != uuid.UUID(vtask_id)).filter(Tasks.title.ilike(FindTitleUnLink))

            notlist_link_task = db.query(Tasks).filter(Tasks.id != vtask_id,Tasks.title.like(search1)).all()
        count_unlink_tasks = len(notlist_link_task)
        if request.method == 'POST':
            btn_unlink = request.POST.get('btn_unlink')
            if btn_unlink:
                # Univers_list.objects.filter(id_in=btn_unlink,id_out=vtask_id).delete()
                DUList = db.query(Univers_list).filter(Univers_list.id_num==int(btn_unlink)).all()
                print('DUList=',DUList,int(btn_unlink))
                if DUList:
                    DUList_ = DUList[0]
                    if DUList_:
                        db.delete(DUList_)
                        db.commit()
                # db.execute(delete(Univers_list).where(Univers_list.id_in==btn_unlink and Univers_list.id_out==vtask_id))
                btn_unlink = None

            btn_link = request.POST.get('btn_link')
            if btn_link:
                lstun = db.query(Univers_list).filter(Univers_list.id_in==uuid.UUID(btn_link), Univers_list.id_out==vtask_id,
                                                      Univers_list.role=='arrow').all()
                # print('len.lstun=',len(lstun))
                # if Univers_list.objects.filter(id_in=btn_link, id_out=vtask_id, role='arrow'):
                if len(lstun)!=0:
                    return HttpResponse("Задачи уже связаны")
                else:
                    lst3 = db.query(Univers_list).filter(Univers_list.id_out == vtask_id ,  Univers_list.role=='arrow').all()
                    max_indx_int = len(lst3)
                    if not max_indx_int:
                        max_indx_int = 0
                    max_indx_int += 1
                    # print(max_indx)
                    NewUlist = Univers_list(id_in=uuid.UUID(btn_link), id_out=vtask_id, num_in_link=max_indx_int, role='arrow')
                    # Univers_list.objects.create(id_in=btn_link, id_out=vtask_id, num_in_link=max_indx_int, role='arrow')
                    db.add(NewUlist)
                    db.commit()
                btn_link = None
    else:
        return HttpResponse("Задача не найдена")

    info_task = {'task_id': vtask_id, 'task_title': vtask_title, 'task_start':vtask_start,
                'task_end': vtask_end,'list_link_task': flist_link_task,
                 'notlist_link_task': notlist_link_task, 'FindTitleUnLink': FindTitleUnLink,
                 'FindTitle': FindTitle,
                 'count_link_tasks': count_link_tasks,'count_unlink_tasks': count_unlink_tasks}
    return render(request,'card_task.html',context=info_task)
def VContactsTask(request, task_id):
    # vtask_id, vtask_title, vtask_start, vtask_end = db.scalar(select(Tasks.id,Tasks.title, Tasks.start, Tasks.end).where(Tasks.id == task_id))
    # find_task = Tasks.objects.filter(id=task_id)
    VTask = db.query(Tasks).filter(Tasks.id == uuid.UUID(task_id)).all()[0]
    vtask_id = VTask.id
    vtask_title = VTask.title
    vtask_start = VTask.start
    vtask_end = VTask.end

    lst_field_task = {'task_id': vtask_id, 'task_title': vtask_title, 'task_start': vtask_start, 'task_end': vtask_end}
    count_link_tasks = 0
    count_unlink_tasks = 0
    # print(type(vtask_id),vtask_id,task_id)
    # info_task = {}
    # if vtask_id==task_id:
    FindTitleUnLink = ''
    FindTitle = ''
    # lst_contacts_rol = []
    notlist_link_task = None
    if vtask_id:
        count_fulllink_task = len(db.query(Univers_list).filter(Univers_list.id_out == vtask_id, Univers_list.role!='arrow').all())
        # link_task = db.query(Univers_list).filter(Univers_list.id_out==vtask_id)
        # count_fulllink_task = link_task.count()
        if request.method == 'POST':
            btn_find_unlink = request.POST.get('btn_find_unlink')
            if btn_find_unlink:
                FindTitleUnLink = request.POST.get('FindTitleUnlink')
                btn_find_unlink = None
            btn_find_tlink = request.POST.get('btn_find_tsklink')
            if btn_find_tlink:
                FindTitle = request.POST.get('FindTitle')
                btn_find_tlink = None
                # print('FindTitle=',FindTitle)
        search = "%{}%".format(FindTitle)
        if count_fulllink_task>0:

            flist_link_task = db.query(Contacts).join(Univers_list, Contacts.id == Univers_list.id_in).filter(Univers_list.id_out == vtask_id, Contacts.last_name.like(search)).all()
            count_link_tasks = len(flist_link_task)

        else:
            flist_link_task = None
        search1 = "%{}%".format(FindTitleUnLink)
        notlist_link_task = db.query(Contacts).filter(Contacts.last_name.like(search1)).all()

        count_unlink_tasks = len(notlist_link_task)
        if request.method == 'POST':
            btn_unlink = request.POST.get('btn_unlink')
            if btn_unlink:
                # Univers_list.objects.filter(id=btn_unlink).delete()
                # db.execute(delete(Univers_list).where(Univers_list.id==btn_unlink ))
                DUList = db.query(Univers_list).filter(Univers_list.id_num==int(btn_unlink)).all()
                DUList_ = DUList[0]
                if DUList_:
                    db.delete(DUList_)
                    db.commit()
                btn_unlink = None

            btn_link = request.POST.get('btn_link')
            btn_role = request.POST.get('btn_role')
            if btn_role:
                # print(vrole)
                vrole = request.POST.get(f"contact_role>{btn_role}")
                # db.execute(update(Univers_list).where(Univers_list.id==Univers_list).values(Univers_list.role=vrole))
                UpUList = db.query(Univers_list).filter(Univers_list.id_num==int(btn_role)).first()
                UpUList.role = vrole
                db.commit()
                btn_role = None
            else:
                vrole = ''

            if btn_link:
                NewUList = Univers_list(id_in=uuid.UUID(btn_link), id_out=vtask_id, num_in_link=0, role=vrole)
                # Univers_list.objects.create(id_in=btn_link, id_out=vtask_id, num_in_link=0, role=vrole)
                db.add(NewUList)
                db.commit()
                btn_link = None
    else:
        return HttpResponse("Задача не найдена")

    info_task = {'task_id': vtask_id, 'task_title': vtask_title, 'task_start':vtask_start,
                'task_end': vtask_end,'list_link_task': flist_link_task,
                 'notlist_link_task': notlist_link_task, 'FindTitleUnLink': FindTitleUnLink,
                 'FindTitle': FindTitle,
                 'count_link_tasks': count_link_tasks,'count_unlink_tasks': count_unlink_tasks}
    return render(request,'task_contacts.html',context=info_task)
