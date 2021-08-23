from .models import Post, Blog, Tweet, CodeGist

def get_user_posts(user):
    user_profile = user.profile
    # Gets the queryset of user posts
    posts = Post.objects.filter(posted_by=user)
    
    # Gets the queryset of user's friends posts
    for profile in user_profile.friends.all() : 
       posts = posts | Post.objects.filter(posted_by=profile)

    # Orders them by created date
    posts.order_by('posted_on')

    final_posts = []

    # Collects the sub posts of the parent post
    for post in posts:
        if post.post_type == "TWEET" :
            sub_post = Tweet.objects.get(post_ref=post)
        elif post.post_type == "BLOG" :
            sub_post = Blog.objects.get(post_ref=post)
        elif post.post_type == "CODEGIST" :
            sub_post = CodeGist.objects.get(post_ref=post)
        final_posts.append({
            'author' : post.posted_by,
            'posted_on' : post.posted_on,
            'post_type' : post.post_type,
            'sub_post' : sub_post
        })

    # Reverses the list such that latest posts come at the top
    final_posts.reverse()

    return final_posts 
      

def is_friend(logged_user, another_user):
    for user in logged_user.profile.friends.all():
        if user == another_user:
            return True
    return False