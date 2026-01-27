from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Category, Product, Order, News, Comment


def home(request):
    latest_products = Product.objects.all()[:5]
    latest_news = News.objects.all()[:3]
    return render(request, 'nike/home.html', {
        'products': latest_products,
        'news': latest_news
    })



def user_list(request):
    users = User.objects.all()
    return render(request, 'nike/user_list.html', {'users': users})


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'nike/user_detail.html', {'user': user})


def user_create(request):
    if request.method == 'POST':
        user = User.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            profile_image=request.FILES.get('profile_image')
        )
        return redirect('user_list')

    return render(request, 'nike/user_form.html')


def user_update(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)

        if request.POST.get('password'):
            user.password = request.POST.get('password')

        if request.FILES.get('profile_image'):
            user.profile_image = request.FILES.get('profile_image')

        user.save()
        return redirect('user_list')

    return render(request, 'nike/user_form.html', {'user': user})


def user_delete(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'nike/user_delete.html', {'user': user})



def category_list(request):
    categories = Category.objects.all()
    return render(request, 'nike/category_list.html', {'categories': categories})


def category_detail(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category_id=id)
    return render(request, 'nike/category_detail.html', {
        'category': category,
        'products': products
    })
def category_create(request):
    if request.method == 'POST':
        Category.objects.create(
            name=request.POST['name'],
            parent_id=request.POST.get('parent')
        )
        return redirect('category_list')

    return render(request, 'nike/category_form.html')


def category_update(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        category.name = request.POST.get('name', category.name)
        category.save()
        return redirect('category_list')

    return render(request, 'nike/category_form.html', {'category': category})


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'nike/product_list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'nike/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            image=request.FILES.get('image'),
            category=get_object_or_404(Category, id=request.POST['category']),
            stock=request.POST['stock']
        )
        return redirect('product_list')

    categories = Category.objects.all()
    return render(request, 'nike/product_form.html', {'categories': categories})


def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.name = request.POST.get('name', product.name)
        product.description = request.POST.get('description', product.description)
        product.price = request.POST.get('price', product.price)

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.category = get_object_or_404(Category, id=request.POST['category'])
        product.stock = request.POST.get('stock', product.stock)

        product.save()
        return redirect('product_list')

    categories = Category.objects.all()
    return render(request, 'nike/product_form.html', {
        'product': product,
        'categories': categories
    })


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')



def news_list(request):
    news_items = News.objects.all()
    return render(request, 'nike/news_list.html', {'news_items': news_items})


def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    comments = news_item.comment_set.all()

    return render(request, 'nike/news_detail.html', {
        'news_item': news_item,
        'comments': comments
    })


def news_create(request):
    if request.method == 'POST':
        News.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            image=request.FILES.get('image')
        )
        return redirect('news_list')

    return render(request, 'nike/news_form.html')


def news_update(request, id):
    news_item = get_object_or_404(News, id=id)

    if request.method == 'POST':
        news_item.title = request.POST.get('title', news_item.title)
        news_item.content = request.POST.get('content', news_item.content)

        if request.FILES.get('image'):
            news_item.image = request.FILES.get('image')

        news_item.save()
        return redirect('news_list')

    return render(request, 'nike/news_form.html', {'news_item': news_item})


def news_delete(request, id):
    news_item = get_object_or_404(News, id=id)
    news_item.delete()
    return redirect('news_list')


def add_comment(request, news_id):
    if request.method == 'POST':
        news_item = get_object_or_404(News, id=news_id)

        Comment.objects.create(
            user=request.user,
            news=news_item,
            content=request.POST['content']
        )

        return redirect('news_detail', id=news_id)

    return redirect('news_list')


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.content = request.POST.get('content', comment.content)
        comment.save()
        return redirect('news_detail', id=comment.news.id)

    return render(request, 'nike/update_comment.html', {'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    news_id = comment.news.id
    comment.delete()
    return redirect('news_detail', id=news_id)


from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Order

# =======================
# ORDERS
# =======================

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'nike/order_list.html', {'orders': orders})


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'nike/order_detail.html', {'order': order})


def order_create(request):
    users = User.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        total_amount = request.POST.get('total_amount')
        status = request.POST.get('status')

        # Validate required fields
        if user_id and total_amount and status:
            Order.objects.create(
                user=get_object_or_404(User, id=user_id),
                total_amount=float(total_amount),
                status=status
            )
            return redirect('order_list')
        else:
            error = "Please fill all required fields."
            return render(request, 'nike/order_form.html', {'users': users, 'error': error})

    return render(request, 'nike/order_form.html', {'users': users})


def order_update(request, id):
    order = get_object_or_404(Order, id=id)
    users = User.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        total_amount = request.POST.get('total_amount')
        status = request.POST.get('status')

        if user_id:
            order.user = get_object_or_404(User, id=user_id)
        if total_amount:
            order.total_amount = float(total_amount)
        if status:
            order.status = status

        order.save()
        return redirect('order_list')

    return render(request, 'nike/order_form.html', {
        'order': order,
        'users': users
    })


def order_delete(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'nike/order_delete.html', {'order': order})