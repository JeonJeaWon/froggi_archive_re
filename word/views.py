from django.shortcuts import render, get_object_or_404, redirect
from .models import Word, Hashtag
from django.utils import timezone
# Create your views here.

#아카이브 홈페이지
def main(request):
    return render(request, 'main.html')

#아카이브 홈페이지
def home(request):
    words = Word.objects.all()
    return render(request, 'home.html', {'words' : words})

#필터링
def filter(request):
    value = request.GET['hash_fi']
    if value:
        results = Word.objects.filter(hashtag__name = value)
        if not results:
            return render(request, 'filter.html', {'empty': '검색 결과가 없습니다', 'value': value})
        return render(request, 'filter.html',{ 'results': results, 'value': value})
    else:
        return redirect('home')


#서치
def search(request):
    keyword = request.GET.get('search')
    if keyword:
        result = Word.objects.filter(**{ 'title__contains' :keyword})
        if not result:
            result = Word.objects.filter(**{ 'body__contains' :keyword})
            if not result:
                return render(request, 'search.html', {'empty': '검색 결과가 없습니다'})
        return render(request, 'search.html',{ 'results': result, 'keyword': keyword})
    else:
        words = Word.objects
        return render(request, 'search.html', {'words' : words, 'check':'check'})
        
#서비스 소개
def about(request):
    return render(request, 'about.html')

#게시글 조회
def detail(request, word_id):
    word_detail = get_object_or_404(Word, pk= word_id)
    hashtags = word_detail.hashtag.all()
    return render(request, 'detail.html', {'word':word_detail, 'hashtags':hashtags})

#게시글 추가페이지
def new(request):
    return render(request, 'new.html')

#추가페이지 이용 글 추가
def create(request):
    word = Word()
    word.title = request.GET['title']
    word.body =  request.GET['body']
    word.pup_date =  timezone.datetime.now()
    word.save()

    hashtags = request.GET['hashtags']
    hashtag = hashtags.split(",")
    for tag in hashtag:
        ht = Hashtag.objects.get_or_create(name = tag)
        word.hashtag.add(ht[0])
        
    return redirect('/word/' + str(word.id))

#게시글 삭제
def delete(request, word_id):
    word = get_object_or_404(Word , pk = word_id)
    word.delete()
    return redirect('home')

#게시글 수정 페이지
def edit(request, word_id):
    word_edit = get_object_or_404(Word , pk = word_id)
    return render(request, 'edit.html', {'word' : word_edit})

#수정 페이지 이용 글 수정
def update(request, word_id):
    word = Word.objects.get(pk = word_id)
    word.title = request.POST['title']
    word.body =  request.POST['body']
    word.pup_date =  timezone.datetime.now()
    word.save()
    return redirect('home')

