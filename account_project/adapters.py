from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def authentication_error(self, request, provider_id, error=None, exception=None, extra_context=None):
        print(
            'SocialAccount authentication error!',
            'error',
            request,
            {'provider_id': provider_id, 'error': error.__str__(), 'exception': exception.__str__(), 'extra_context': extra_context},)
        return super().authentication_error(request, provider_id, error, exception, extra_context)