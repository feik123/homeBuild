from homeBuild.accounts.models import HomeOwnerProfile, ContractorProfile


def user_authenticated(request):
    return {
        'user_authenticated': request.user.is_authenticated
    }

def profile_info(request):
    profile_type = None
    homeowner_profile = None
    contractor_profile = None

    if request.user.is_authenticated:
        # Check for homeowner profile
        try:
            homeowner_profile = HomeOwnerProfile.objects.get(user=request.user)
            profile_type = 'homeowner'
        except HomeOwnerProfile.DoesNotExist:
            pass  # If no profile exists, leave homeowner_profile as None

        # Check for contractor profile
        try:
            contractor_profile = ContractorProfile.objects.get(user=request.user)
            profile_type = 'contractor'
        except ContractorProfile.DoesNotExist:
            pass  # If no profile exists, leave contractor_profile as None

    return {
        'profile_type' : profile_type,
        'homeowner_profile' : homeowner_profile,
        'contractor_profile' : contractor_profile,
    }


